"""Model and databasefor memed"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Drug(db.Model):
    """Drug info from openFDA"""

    __tablename__="drugs"

    drug_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    spl_id = db.Column(db.String(64), nullable=False)
    brand_name = db.Column(db.String(200), nullable=False)
    ndc = db.Column(db.String(20), nullable=False)


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


class drugRating(db.Model):
    """Rating of a drug by a user."""

    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    drug_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    score = db.Column(db.Integer)
    comments = db.Column(db.String, nullable= False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Rating rating_id=%s movie_id=%s user_id=%s score=%s>" % (
            self.rating_id, self.movie_id, self.user_id, self.score)



def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drugsfromopenfda.db'
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."




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

