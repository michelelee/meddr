import requests
import json

f = open("secrets.txt")
keys = f.read().strip().split()
openfda_api_key = keys[0]


def search_openfda(keywords):
	api_key = openfda_api_key
	r = requests.get('https://api.fda.gov/drug/label.json?api_key=%s&search=brand_name:%s&limit=100' % (openfda_api_key, keywords)).json()
	
	if 'error' in r:
		raise Exception  

	druglist = r['results']
	count = r['meta']['results']['total']
 	returned_drugs = {}
	
	for drug in druglist:
		print "\n\n"
		spl_id = drug['openfda']['spl_id'][0]
		brand = drug['openfda']['brand_name'][0]
		manufacturer = drug['openfda']['manufacturer_name'][0]
		returned_drugs[spl_id] = {}

		descriptions = [
			'indications_and_usage',
			'how_supplied',
			'dosage_and_administration',
			'description',
			'adverse_reactions',
			'general_precautions',
			'warnings'
			]

		for x in descriptions:
			if x in drug and drug[x].__len__() > 0:
				returned_drugs[spl_id][x] = drug[x][0]


		openfdadescriptions = [
			'product_ndc',
			'substance_name',
			'manufacturer_name',
			'product_type',
			'brand_name',
			'route',
			'generic_name',
			'spl_set_id'
			]

		for x in openfdadescriptions:
			if x in drug['openfda'] and drug['openfda'][x].__len__() > 0:
				returned_drugs[spl_id][x] = drug['openfda'][x][0]

	return returned_drugs, brand, manufacturer, count





