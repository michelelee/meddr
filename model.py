"""Model and databasefor memed"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint

db = SQLAlchemy()


class Donor(db.Model):
    """Drug info from openFDA"""

    __tablename__="drugs"

    donor_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(99999), nullable=False)
    password = db.Column(db.String(64), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    phone = db.Column(db.String(10), nullable=False)
    zipcode = db.Column(db.String(15), nullable=True)
    jobtitle = db.Column(db.String(99999), nullable=False)
    political_aff = db.Column(db.String(99999), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""
        return "<donor_id=%s name=%s jobtitle=%s>" % (self.donor_id, self.name, self.jobtitle)

class Org(db.Model):
    """User of memed website."""

    __tablename__ = "orgs"

    org_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    org_name = db.Column(db.String(64), nullable=True)
    password = db.Column(db.String(64), nullable=True)
    org_url = db.Column(db.String(64), nullable=True)
  

    @staticmethod
    def get_user(org_id):
        user = User.query.filter_by(org_id=org_id).first()
        print  org_id
        print "in get_user static method"
        return org_id


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User =%s email=%s>" % (self.org_id, self.meddr_username)

 






 