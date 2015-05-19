

import requests
import json


def seed_():
	
	brand_name = ''		# request.form.(name of field)

	r = requests.get('https://api.fda.gov/drug/label.json?api_key=DWhqkP2B0GiId0OAuz15UIAvZharbqMrComhRBG1&search=brand_name:%s&limit=10'%brand_name)



	alljson = r.json()

	druglist = alljson['results']
	# print druglist
 	all_drugs = {}

def seed_drugs():
	
	for drug in druglist:
		print drug
		requested_drug = {}
		requested_drug['indications_and_usage'] = drug['indications_and_usage'][0]
		# requested_drug[key_indications] = indications_and_usage

		if 'how_supplied' in drug and drug['how_supplied'].count > 0:
			requested_drug['how_supplied'] = drug['how_supplied'][0]
		requested_drug['dosage_and_administration'] = drug['dosage_and_administration'][0]
		requested_drug['description'] = drug['description'][0]
		#requested_drug['spl_id']= drug['openfda']['spl_id'][0]
		requested_drug['spl_id']= drug['openfda']['spl_id'][0]
		print requested_drug
		requested_drug['substance_name'] = drug['openfda']['substance_name'][0]
		requested_drug['product_type'] = drug['openfda']['product_type'][0]
		requested_drug['brand'] = drug['openfda']['brand_name'][0]
		requested_drug['generic_name'] = drug['openfda']['generic_name'][0]
		# requested_drug['warnings'] = drug['warnings'][0]
		requested_drug['adverse_reactions'] = drug['adverse_reactions'][0]
		# general_precautions = drug['general_precautions'][0]

		all_drugs[requested_drug['spl_id']] = requested_drug

		# changing vs referencing requested_drug... look up


	print requested_drug



		# string = brand + ' by ' + manufacturer
		# brands_manufacturers.join(string)



# make a function called get drug, from this I want to 'store' 




