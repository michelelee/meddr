"""medme"""

# from jinja2 import StrictUndefined
from flask import Flask, render_template, request, session, flash, redirect
from search_openfda import search_openfda
from search_openfda_splid import search_openfda_by_spl_id
import requests
import json

from model import connect_to_db, User, db, Drug, Rating


app = Flask(__name__)
app.secret_key = "ABC"



@app.route("/")
def index():
	"""Homepage and search"""

	return render_template("homepage.html")


@app.route('/register', methods=['GET'])
def register_form():
    """Show meddr form for user signup."""

    return render_template("register.html")


@app.route('/register', methods=['POST'])
def register_process():
    """Process registration."""

    meddr_username =request.form["meddr_username"]
    password = request.form["password"]
    age = int(request.form["age"])
    zipcode = request.form["zipcode"]

    new_user = User(meddr_username=meddr_username, password=password, age=age, zipcode=zipcode)

    db.session.add(new_user)
    db.session.commit()

    flash("User %s added." % meddr_username)
    return redirect("/")


@app.route('/login', methods=['GET'])
def login_form():
    """Show login form."""

    return render_template("login.html")


@app.route('/login', methods=['POST'])
def login_process():
    """Processes login."""

    meddr_username = request.form["meddr_username_input"]
    password = request.form["password_input"]

    user = User.query.filter_by(meddr_username=meddr_username).first()

    if not user:
        flash("Invalid MedDr ID")
        return redirect("/login")

    if user.password != password:
        flash("Incorrect password")
        return redirect("/login")

    session["user_id"] = user.user_id
    session["user_name"] = user.meddr_username

    flash("Logged in")
    return redirect("/")


@app.route('/logout')
def logout():
    """Log out."""

    del session["user_id"]
    flash("Logged Out.")
    return redirect("/")


@app.route('/user')
def get_user_info():
    """Show user profile"""

    user_id = session.get("user_id")

    if user_id:
        all_rated = Rating.query.filter_by(user_id=user_id).all()
        print user_id , all_rated

        render_template("user_profile.html",all_rated=all_rated)

    else:
        flash("Invalid MedDr ID")
        return redirect("/login")



@app.route("/drug_search_results", methods=['POST'])
def search():
    """User inputs drug search here"""
    
    keywords = request.form["drugname_keywords"]

    try:
        returned_drugs, brand, manufacturer, count = search_openfda(keywords)
    except:
        flash("No drug matches found matching '%s'."  % keywords )
        return redirect("/")


    return render_template("drug_search_results.html", keywords=keywords,
                                                        returned_drugs = returned_drugs,
                                                        brand = brand,
                                                        count = count,
                                                        manufacturer = manufacturer )


@app.route("/rate_drug", methods=['POST', 'GET'])
def get_result():
    """Show info about drug.
    If a user is logged in, we will let them add drug feedbadk."""

    spl_set_id = request.values["spl_set_id"]

    avg_score = db.session.query(db.func.avg(Rating.score)).filter_by(spl_set_id=spl_set_id).scalar()

    comments = db.session.query(Rating.comment).filter_by(spl_set_id=spl_set_id).all()

    num_headaches = Rating.query.filter(Rating.spl_set_id==spl_set_id).filter_by(headache=1).count()
    num_body_aches = Rating.query.filter(Rating.spl_set_id==spl_set_id).filter_by(body_aches=1).count()
    num_diarrhea = Rating.query.filter(Rating.spl_set_id==spl_set_id).filter_by(diarrhea=1).count()
    num_constipation = Rating.query.filter(Rating.spl_set_id==spl_set_id).filter_by(constipation=1).count()
    num_vomiting_nausea = Rating.query.filter(Rating.spl_set_id==spl_set_id).filter_by(vomiting_nausea=1).count()
    num_irritable = Rating.query.filter(Rating.spl_set_id==spl_set_id).filter_by(irritable=1).count()
    num_moodiness = Rating.query.filter(Rating.spl_set_id==spl_set_id).filter_by(moodiness=1).count()
    num_drowsiness = Rating.query.filter(Rating.spl_set_id==spl_set_id).filter_by(drowsiness=1).count()
    num_disorientation = Rating.query.filter(Rating.spl_set_id==spl_set_id).filter_by(disorientation=1).count()
    num_bloating_swelling = Rating.query.filter(Rating.spl_set_id==spl_set_id).filter_by(bloating_swelling=1).count()
    num_skin_reactions = Rating.query.filter(Rating.spl_set_id==spl_set_id).filter_by(skin_reactions=1).count()
    num_chills_sweating = Rating.query.filter(Rating.spl_set_id==spl_set_id).filter_by(chills_sweating=1).count()
    num_dizziness = Rating.query.filter(Rating.spl_set_id==spl_set_id).filter_by(dizziness=1).count()
    num_weight_gain = Rating.query.filter(Rating.spl_set_id==spl_set_id).filter_by(weight_gain=1).count()
    num_weight_loss = Rating.query.filter(Rating.spl_set_id==spl_set_id).filter_by(weight_loss=1).count()

    user_side_effects = [num_headaches, num_body_aches, num_diarrhea, num_constipation, num_vomiting_nausea, num_irritable, num_moodiness,num_drowsiness, num_disorientation, num_bloating_swelling, num_skin_reactions, num_chills_sweating, num_dizziness, num_weight_gain, num_weight_loss]

    side_effect_list = ['headaches', 'bodyaches', 'diarrhea', 'constipation', 'vomiting_nausea','irritable', 'moodiness', 'drowsiness', 'disorientation', 'bloating_swelling', 'skin_reactions', 'chills_sweating', 'dizziness', 'weight_gain', 'weight_loss']
    
    print "side effect list:", side_effect_list


    print "user side effects :", user_side_effects
   

    print "headaches", num_headaches
    print "bodyaches", num_body_aches

    user_id = session.get("user_id")

    user = User.get_user(user_id=user_id)
    print user

    if user is None: 
        flash("Invalid MedDr ID")
        return redirect("/login")

    if user_id:
        user_rating = Rating.query.filter_by(spl_set_id=spl_set_id, user_id=user_id).first()
    else:
        user_rating = None

    drug = Drug.query.filter_by(spl_set_id=spl_set_id).first()

    if drug:
        session["spl_set_id"] = drug.spl_set_id

        return render_template("rate_drug.html",drug=drug,
                                                user=user,
                                                user_rating=user_rating,
                                                avg_score=avg_score,
                                                comments=comments, 
                                                user_side_effects=user_side_effects, 
                                                side_effect_list=side_effect_list
                                                )
    else:
        search_openfda_by_spl_id(spl_set_id)

        drug = Drug.query.filter_by(spl_set_id=spl_set_id).first()

        session["spl_set_id"] = drug.spl_set_id

        return render_template("rate_drug.html",drug=drug,
                                                user=user,
                                                user_id=user_id,
                                                user_rating=user_rating,
                                                avg_score=avg_score,
                                                comments=comments, 
                                                user_side_effects=user_side_effects, 
                                                side_effect_list=side_effect_list
                                                )

@app.route("/add_drug_feedback", methods=['POST'])
def drug_details_process():
    """Add/edit a rating."""

    spl_set_id = session.get('spl_set_id')

    thisdrug = Drug.query.get(spl_set_id)

    score = int(request.form["score"])

    comment = request.form["comment"]

    side_effect = request.form.getlist('side_effect')

    user_id = session.get("user_id")

    rating = Rating.query.filter_by(user_id=user_id, spl_set_id=spl_set_id).first()

    if not rating:
        rating = Rating(user_id=user_id, spl_set_id=spl_set_id)

    rating.score = score
    rating.comment = comment
       
    rating.reset_side_effect()

    for item in side_effect:
        rating.add_side_effect(item)

    db.session.add(rating)
    db.session.commit()

    return redirect("/rate_drug?spl_set_id=%s" % spl_set_id)


if __name__ == "__main__":

    app.debug = True
    connect_to_db(app)
    app.run(use_debugger=True, debug=app.debug)
