# from server import app 

import requests
import json

f = open("secrets.txt")
keys = f.read().strip().split()
openfda_api_key = keys[0]




def search_openfda(keywords):

	api_key = openfda_api_key
	
	
	r = requests.get('https://api.fda.gov/drug/label.json?api_key=%s&search=brand_name:%s&limit=100' % (openfda_api_key, keywords)).json()

	# r = requests.get().json() #if i get no attribute __getitem__ im missing the () parenx

	druglist = r['results']
	count = r['meta']['results']['total']
	# print count
 	returned_drugs = {}
	
	for drug in druglist:
		# print drug['openfda']['brand_name']
		spl_id = drug['openfda']['spl_id'][0]

		returned_drugs[spl_id] = {
		# 'indications_and_usage' : drug['indications_and_usage'][0],
		# requested_drug[key_indications] = indications_and_usage
		# if 'how_supplied' in drug and drug['how_supplied'].count > 0:
		# 'how_supplied' : drug['how_supplied'][0],
		# 'dosage_and_administration' : drug['dosage_and_administration'][0],
		# 'description' : drug['description'][0],
		# adverse_reactions = drug['adverse_reactions'][0]
		# general_precautions = drug['general_precautions'][0]
		#requested_drug['spl_id']= drug['openfda']['spl_id'][0]
		
		# warnings = drug['warnings'][0]
		'product_ndc' : drug['openfda']['product_ndc'][0],
		'substance_name' : drug['openfda']['substance_name'][0],
		'manufacturer_name' : drug['openfda']['manufacturer_name'][0],
		'product_type' : drug['openfda']['product_type'][0],
		'brand' : drug['openfda']['brand_name'][0],
		'route' : drug['openfda']['route'][0],
		'generic_name' : drug['openfda']['generic_name'][0]
		}
		

		# all_drugs[requested_drug['spl_id']] = requested_drug

		# chaning vs referencing requested_drug... look up

		# db.session.add(drug)
		
	return returned_drugs , count
	

	# print requested_drug



		# string = brand + ' by ' + manufacturer
		# brands_manufacturers.join(string)



# make a function called get drug, from this I want to 'store' 




