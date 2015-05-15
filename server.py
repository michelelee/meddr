# """Medme"""

# from flask import flask

# from model import connect_to_db, connect_to_db

# app = Flask (__name__)

import requests

# # jinja, render template

# @app.route("/")
# def show_form():

# return render_template("blah form.html")



# @app.route("/", methods=["POST"])
def get_drug_mfg():

	brand_name = 'viagra'

	# request.form.(name of field)

	# payload = {'limit' : '100', 'brand_name' : '"viagra"'}
	
	r = requests.get('https://api.fda.gov/drug/label.json?api_key=DWhqkP2B0GiId0OAuz15UIAvZharbqMrComhRBG1&search=brand_name:%s&limit=100' %brand_name)

	# search=brand_name:&limit=300" %(userinput) 


	alljson = r.json()

	druglist = alljson['results']

	brands_manufacturers = " "




	for drug in druglist:
		brand = drug["brand_name"]
		manufacturer = drug['manufacturer_name']
		string = brand + ' by ' + manufacturer
		brands_manufacturers.add(string)

	print brands_manufacturers

	print 'hello'

	return brands_manufacturers







# @app.route("/", methods=["POST"])
# def get_indications():

# 	brand_name = request.form.(name of field)

# 	# payload = {'limit' : '100', 'brand_name' : '"viagra"'}



# 	r = requests.get('https://api.fda.gov/drug/label.json?api_key=DWhqkP2B0GiId0OAuz15UIAvZharbqMrComhRBG1&search=brand_name:%s&limit=300' %brand_name)

# 	# search=brand_name:&limit=300" %(userinput) 


# 	results = r.json()

# 	for indication in indications 
# 		indications = results[0]['indications_and_usage'][0]

# 	return render_template("blah.html",indications=indications)





# print r.url	