"""Model and databasefor memed"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint

db = SQLAlchemy()


class Drug(db.Model):
    """Drug info from openFDA"""

    __tablename__="drugs"

    # drug_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    spl_set_id = db.Column(db.String(64), primary_key=True)
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
        return "<spl_set_id=%s generic_name=%s brand_name=%s>" % (self.spl_set_id, self.generic_name, self.brand_name)

        # return "<Drug_id=%s spl_set_id=%s manufacturer_name=%s product_type=%s description=%s dosage_and_administration=%s route=%s generic_name=%s brand_name=%s substance_name=%s product_ndc=%s adverse_reactions=%s how_supplied=%s indications_and_usage=%s >" % (self.drug_id, self.spl_set_id, self.manufacturer_name, self.product_type, self.description, self.dosage_and_administration, self.route, self.generic_name, self.brand_name, self.substance_name, self.product_ndc, self.adverse_reactions, self.how_supplied, self.indications_and_usage)


class User(db.Model):
    """User of memed website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    meddr_username = db.Column(db.String(64), nullable=True)
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
    spl_set_id = db.Column(db.String(64), db.ForeignKey('drugs.spl_set_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    score = db.Column(db.Integer)
    comment = db.Column(db.String, nullable= False)
    headache = db.Column(db.Integer, default=0)
    stomach_pain = db.Column(db.Integer, default=0)
    body_aches = db.Column(db.Integer, default=0)
    diarrhea = db.Column(db.Integer, default=0)
    constipation = db.Column(db.Integer, default=0)
    vomiting_nausea = db.Column(db.Integer, default=0)
    moodiness = db.Column(db.Integer, default=0)
    drowsiness = db.Column(db.Integer, default=0)
    disorientation = db.Column(db.Integer, default=0)
    bloating_swelling = db.Column(db.Integer, default=0)
    skin_reactions = db.Column(db.Integer, default=0)
    chills_sweating = db.Column(db.Integer, default=0)
    dizziness = db.Column(db.Integer, default=0)
    weight_gain = db.Column(db.Integer, default=0)
    weight_loss = db.Column(db.Integer, default=0)


    __table_args__ = (CheckConstraint(score.in_(range(1, 11))), )

    user = db.relationship("User",
                           backref=db.backref("ratings", order_by=rating_id))

    drug = db.relationship("Drug",
                            backref=db.backref("ratings", order_by=rating_id))

    def add_side_effect(self, side_effect=None):
        if side_effect == "headache":
            self.headache = 1
            print "hello there"
        elif side_effect == "stomach_pain":
            self.stomach_pain = 1
        elif side_effect == "body_aches":
            self.body_aches = 1
        elif side_effect == "diarrhea":
            self.diarrhea = 1
        elif side_effect == "constipation":
            self.constipation = 1
        elif side_effect == "vomiting_nausea":
            self.vomiting_nausea = 1
        elif side_effect == "moodiness":
            self.moodiness = 1
        elif side_effect == "drowsiness":
            self.drowsiness = 1
        elif side_effect == "disorientation":
            self.disorientation = 1
        elif side_effect == "bloating_swelling":
            self.bloating_swelling = 1
        elif side_effect == "skin_reactions":
            self.skin_reactions = 1
        elif side_effect == "chills_sweating":
            self.chills_sweating = 1
        elif side_effect == "dizziness":
            self.dizziness = 1
        elif side_effect == "weight_gain":
            self.weight_gain = 1
        elif side_effect == "weight_loss":
            self.weight_loss = 1
        else:
            pass

    def reset_side_effect(self):
        self.headache = 0
        self.stomach_pain = 0
        self.body_aches = 0
        self.diarrhea = 0
        self.constipation = 0
        self.vomiting_nausea = 0
        self.moodiness = 0
        self.drowsiness = 0
        self.disorientation = 0
        self.bloating_swelling = 0
        self.skin_reactions = 0
        self.chills_sweating = 0
        self.dizziness = 0
        self.weight_gain = 0
        self.weight_loss = 0


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Rating rating_id=%s spl_set_id=%s user_id=%s score=%s>" % (
            self.rating_id, self.spl_set_id, self.user_id, self.score)



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

