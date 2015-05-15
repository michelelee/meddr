"""Model and databasefor memed"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """User of memed website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(64), nullable=True)
    password = db.Column(db.String(64), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    zipcode = db.Column(db.String(15), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User user_id=%s email=%s>" % (self.user_id, self.email)


class Rating(db.Model):
    """Rating of a drug by a user."""

    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    drug_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    score = db.Column(db.Integer)
    review = db.Column(db.String, nullable= False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Rating rating_id=%s movie_id=%s user_id=%s score=%s>" % (
            self.rating_id, self.movie_id, self.user_id, self.score)













# import requests

# # jinja, render template

# @app.route("/")
# def show_form():

# 	return render_template("blah form.html")


# @app.route("/", methods=["POST"])
# def get_indications():

# 	brand_name = cookie


# 	# request.form.(name of field)

# 	# payload = {'limit' : '100', 'brand_name' : '"viagra"'}



# 	r = requests.get('https://api.fda.gov/drug/label.json?api_key=DWhqkP2B0GiId0OAuz15UIAvZharbqMrComhRBG1&search=brand_name:%s&limit=200' %brand_name)

# 	# search=brand_name:&limit=300" %(userinput) 




# 	results = r.json()

# 	indications = results[0]['indications_and_usage'][0]

# 	return render_template("blah.html",indications=indications)




# print r.url	


	


# write a function that will take in a brand name and print out the indications and usage for each result from the openFDA api

