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

    def __repr__(self):
        """Provide helpful representation when printed."""
        return "<spl_set_id=%s generic_name=%s brand_name=%s>" % (self.spl_set_id, self.generic_name, self.brand_name)

class Org(db.Model):
    """User of memed website."""

    __tablename__ = "users"

    org_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    org_name = db.Column(db.String(64), nullable=True)
    password = db.Column(db.String(64), nullable=True)
    org_url = db.Column(db.String(64), nullable=True)
  

    @staticmethod
    def get_user(org_id):
        user = User.query.filter_by(org_id=org_id).first()
        print  user
        print "in get_user static method"
        return user


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User user_id=%s email=%s>" % (self.user_id, self.meddr_username)


class Rating(db.Model):
    """Rating of a drug by a user."""

    __tablename__ = "ratings"




    __table_args__ = (CheckConstraint(score.in_(range(1, 11))), )

    user = db.relationship("User",
                           backref=db.backref("ratings", order_by=rating_id))

    drug = db.relationship("Drug",
                            backref=db.backref("ratings", order_by=rating_id))