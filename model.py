"""Model and databasefor memed"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Drug(db.Model):
    """Drug info from openFDA"""

    __tablename__="drugs"

    drug_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    spl_set_id = db.Column(db.String(64), nullable=False, unique=True)
    manufacturer_name = db.Column(db.String(99999), nullable=False)
    product_type = db.Column(db.String(99999), nullable=False)
    description = db.Column(db.String(99999), nullable=False)
    dosage_and_administration = db.Column(db.String(99999), nullable=False)
    route = db.Column(db.String(99999), nullable=False)
    generic_name = db.Column(db.String(99999), nullable=False)
    brand_name = db.Column(db.String(200), nullable=False) 
    substance_name = db.Column(db.String(99999), nullable=False)
    product_ndc = db.Column(db.String(20), nullable=False)
    adverse_reactions = db.Column(db.String(99999), nullable=False)
    how_supplied = db.Column(db.String(99999), nullable=False)
    indications_and_usage = db.Column(db.String(99999), nullable=False)


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Drug_id=%s spl_set_id=%s manufacturer_name=%s product_type=%s description=%s dosage_and_administration=%s route=%s generic_name=%s brand_name=%s substance_name=%s product_ndc=%s adverse_reactions=%s how_supplied=%s indications_and_usage=%s >" % (self.drug_id, self.spl_set_id, self.manufacturer_name, self.product_type, self.description, self.dosage_and_administration, self.route, self.generic_name, self.brand_name, self.substance_name, self.product_ndc, self.adverse_reactions, self.how_supplied, self.indications_and_usage)


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
    comment = db.Column(db.String, nullable= False)

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

