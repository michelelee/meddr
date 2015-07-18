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

def create_donations():
	donated_at = forgery_py.forgery.date.date(past=True, min_delta=0, max_delta=600)
	donation_amt = random.randint(5, 2000)
	donor_id = random.randrange(1, 100)
	org_id = random.randrange(1, 5)
	campaign_id = random.randrange(1, 3)

	a_donation = Donation(donated_at = donated_at,
							donation_amt = donation_amt,
							donor_id = donor_id,
							org_id = org_id,
							campaign_id = campaign_id)

	db.session.add(a_donation)

def create_orgs():
	
	org_name = "Coding for Kids"
	password = forgery_py.forgery.basic.text(length=None,
			at_least=3, at_most=15, lowercase=True, uppercase=True, 
			digits=False, spaces=False, punctuation=False)
	org_url = forgery_py.forgery.internet.top_level_domain()

	an_org = Org(org_name = org_name,
				password = password,
				org_url = org_url)

	db.session.add(an_org)

	def random_orgs():
		org_name = forgery_py.forgery.basic.text(length=None,
			at_least=3, at_most=15, lowercase=True, uppercase=True, 
			digits=False, spaces=True, punctuation=False)
		password = forgery_py.forgery.basic.text(length=None,
			at_least=3, at_most=15, lowercase=True, uppercase=True, 
			digits=False, spaces=False, punctuation=False)
		org_url = forgery_py.forgery.internet.top_level_domain()

		an_org = Org(org_name = org_name,
					password = password,
					org_url = org_url)

		db.session.add(an_org)

		for i in range(4):
			random_orgs()


def create_campaigns():
	stem = Campaign(campaign_name = "STEM Program for Girls",
		target_amt = 50000,
		description = forgery_py.forgery.lorem_ipsum.paragraph(separator='\n\n', wrap_start='', wrap_end='', html=False, sentences_quantity=3),
		issue_area = "Education")
	hour_of_code = Campaign(campaign_name = "Hour of Code",
		target_amt = 10000,
		description = forgery_py.forgery.lorem_ipsum.paragraph(separator='\n\n', wrap_start='', wrap_end='', html=False, sentences_quantity=3),
		issue_area = "Education")
	higher_ed = Campaign(campaign_name = "Road to Higher Education",
		target_amt = 20000,
		description = forgery_py.forgery.lorem_ipsum.paragraph(separator='\n\n', wrap_start='', wrap_end='', html=False, sentences_quantity=3),
		issue_area = "Education")

	db.session.add(stem)
	db.session.add(hour_of_code)
	db.session.add(higher_ed)



if __name__ == "__main__":
	connect_to_db(app)

	for i in range(100):
		create_donors()

	for i in range(150):
		create_donations()

	create_orgs()
	create_campaigns()

	db.session.commit()

