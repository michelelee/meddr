"""Model and databasefor memed"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint

db = SQLAlchemy()


class Donor(db.Model):
    """Individual donors that donate to campaigns and 501(c)s"""

    __tablename__="donors"

    donor_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(99999), nullable=False)
    # password = db.Column(db.String(64), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    phone = db.Column(db.String(10), nullable=False)
    zipcode = db.Column(db.String(15), nullable=True)
    jobtitle = db.Column(db.String(500), nullable=False)
    political_aff = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return "<Donor: name=%s>" % (self.name)

class Org(db.Model):
    """501(c) organizations - recipients of donations"""

    __tablename__ = "orgs"

    org_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    org_name = db.Column(db.String(64), nullable=True)
    password = db.Column(db.String(64), nullable=True)
    org_url = db.Column(db.String(64), nullable=True)


    def __repr__(self):
        return "<Org: org_name=%s>" % (self.org_name)


class Donation(db.Model):
    """Donation objects - links together donors, 501(c)s, and campaigns"""

    __tablename__ = "donations"

    donation_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    donated_at = db.Column(db.DateTime(64), nullable=True)
    donor_id = db.Column(db.Integer, db.ForeignKey("donors.donor_id"))
    org_id = db.Column(db.Integer, db.ForeignKey("orgs.org_id"))
    campaign_id = db.Column(db.Integer, db.ForeignKey("campaigns.campaign_id"))

    def __repr__(self):
        return "<Donation: donation_id=%s, donated_at=%s>" % (self.donation_id, self.donated_at)


class Campaign(db.Model):
    """Campaigns that organizations can support"""

    __tablename__ = "campaigns"

    campaign_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    target_amt = db.Column(db.Float, nullable = False)
    description = db.Column(db.String(99999))
    issue_area = db.Column(db.String(100))


