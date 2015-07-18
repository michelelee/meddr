import forgery_py
import random
from model import Donor, Org, Donation, Campaign, connect_to_db, db
from server import app


political_parties = ['Democrat', 'Republican', 'Independant', 'Libertarian', 'Green', 'Constitution']

def create_donors():
	a_donor = Donor(name = forgery_py.name.full_name(),
					age = random.randrange(18, 90),
					phone = forgery_py.forgery.address.phone(),
					zipcode = forgery_py.forgery.address.zip_code(),
					jobtitle = forgery_py.forgery.name.job_title(),
					political_aff = random.choice(political_parties))

	db.session.add(a_donor)
	db.session.commit()

def create_donations():
	a_donation = (donated_at

def create_orgs():
	pass

def create_campaigns():
	pass


if __name__ == "__main__":
	connect_to_db(app)

	for i in range(100):
		create_donors()

