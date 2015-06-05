"""medme"""

# from jinja2 import StrictUndefined
# import search_openFDA import seed_drugs seeds_drugs.variable name 
from flask import Flask, render_template, request, session, flash, redirect
from search_openfda import search_openfda
from search_openfda_splid import search_openfda_by_spl_id
import requests
import json


 # session, redirect

from model import connect_to_db, User, db, Drug, Rating
# from search_openFDA import 

app = Flask(__name__)
app.secret_key = "ABC"

# app.jinja_env.undefined = StrictUndefined

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

    # Get form variables
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
    """Process login."""

    # Get form variables
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

    flash("Logged in")
    return redirect("/")

@app.route('/logout')
def logout():
    """Log out."""

    del session["user_id"]
    flash("Logged Out.")
    return redirect("/")


@app.route("/drug_search_results", methods=['POST'])
#if you land on /drug_seearch resutls from a post request, do this search 
def search():
    """User inputs drug search here"""
    
    keywords = request.form["drugname_keywords"]
    print keywords

    returned_drugs, brand, manufacturer, count = search_openfda(keywords)
    print type(returned_drugs)


# or the returned drugs will be in json 
    return render_template("drug_search_results.html", returned_drugs = returned_drugs,
                                                        brand = brand,
                                                        count = count,
                                                        manufacturer = manufacturer )

@app.route("/rate_drug", methods=['POST', 'GET'])
def get_result():
    """Show info about drug.

    If a user is logged in, we will let them add drug feedbadk.
    """


    spl_set_id = request.values["spl_set_id"]


    # spl_set_id = request.form.get("spl_set_id", request.args["spl_set_id"])


    user_id = session.get("user_id")

    if user_id:
        user_rating = Rating.query.filter_by(
            spl_set_id=spl_set_id, user_id=user_id).first()
    else:
        user_rating = None


    drug = Drug.query.filter_by(spl_set_id=spl_set_id).first()

    if drug:
        session["spl_set_id"] = drug.spl_set_id

        return render_template("rate_drug.html",drug=drug,
                                                user_id=user_id,
                                                user_rating=user_rating
                                                 )

    else:
        search_openfda_by_spl_id(spl_set_id)

        drug = Drug.query.filter_by(spl_set_id=spl_set_id).first()

        session["spl_set_id"] = drug.spl_set_id

        return render_template("rate_drug.html",drug=drug,
                                        user_id=user_id,
                                        user_rating=user_rating
                                                 )

@app.route("/add_drug_feedback", methods=['POST'])
def drug_details_process():
    """Add/edit a rating."""

    spl_set_id = session.get('spl_set_id')
    print spl_set_id

    score = int(request.form["score"])
    print score

    comment = request.form["comment"]
    print comment 

    user_id = session.get("user_id")

    rating = Rating.query.filter_by(user_id=user_id, spl_set_id=spl_set_id).first()

    if rating:
        rating.score = score
        flash("Rating updated.")

    else:
        rating = Rating(user_id=user_id, spl_set_id=spl_set_id, score=score, comment=comment)
        flash("feedbadk added.")
        db.session.add(rating)

    db.session.commit()

    return redirect("/rate_drug?spl_set_id=%s" % spl_set_id)

    # return "drug added to database"


if __name__ == "__main__":

    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension

    # Do not debug for demo
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run(use_debugger=True, debug=app.debug)



# spl_set_id=spl_set_id,
#                                                 manufacturer_name=manufacturer_name,
#                                                 product_type=product_type,
#                                                 description=description,
#                                                 dosage_and_administration=dosage_and_administration,
#                                                 route=route,
#                                                 generic_name=generic_name,
#                                                 brand_name=brand_name,
#                                                 substance_name=substance_name,
#                                                 product_ndc=product_ndc,
#                                                 adverse_reactions=adverse_reactions,
#                                                 how_supplied=how_supplied,
#                                                 indications_and_usage=indications_and_usage, 
#                                                 avg_rating=avg_rating,



#             spl_set_id = drug.spl_set_id
#         manufacturer_name = drug.manufacturer_name
#         product_type =drug.product_type
#         description =drug.description
#         dosage_and_administration =drug.dosage_and_administration
#         route =drug.route
#         generic_name =drug.generic_name
#         brand_name = drug.brand_name
#         substance_name = drug.substance_name
#         product_ndc = drug.product_ndc
#         adverse_reactions =drug.adverse_reactions
#         how_supplied =drug.how_supplied
#         indications_and_usage =drug.indications_and_usage