# from server import app
import requests
import json

f = open("secrets.txt")
keys = f.read().strip().split()
openfda_api_key = keys[0]




def search_openfda(keywords):
	api_key = openfda_api_key
	r = requests.get('https://api.fda.gov/drug/label.json?api_key=%s&search=brand_name:%s&limit=100' % (openfda_api_key, keywords)).json()
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

		returned_drugs[spl_id]['json']= json.dumps(drug)


		# if 'product_ndc' in drug['openfda'] and drug['openfda']['product_ndc'].__len__() > 0:
		# 	returned_drugs[spl_id]['NDC'] = drug['openfda']['product_ndc'][0]

		# if 'substance_name' in drug['openfda'] and drug['openfda']['substance_name'].__len__() > 0:
		# 	returned_drugs[spl_id]['Chemical Name'] = drug['openfda']['substance_name'][0]

		# if 'manufacturer_name' in drug['openfda'] and drug['openfda']['manufacturer_name'].__len__() > 0:
		# 	returned_drugs[spl_id]['Manufacturer'] = drug['openfda']['manufacturer_name'][0]

		# if 'product_type' in drug['openfda'] and drug['openfda']['product_type'].__len__() > 0:
		# 	returned_drugs[spl_id]['Intended User'] = drug['openfda']['product_type'][0]

		# if 'brand_name' in drug['openfda'] and drug['openfda']['brand_name'].__len__() > 0:
		# 	returned_drugs[spl_id]['Brand Name'] = drug['openfda']['brand_name'][0]

		# if 'route' in drug['openfda'] and drug['openfda']['route'].__len__() > 0:
		# 	returned_drugs[spl_id]['Administraion Route'] = drug['openfda']['route'][0]

		# if 'generic_name' in drug['openfda'] and drug['openfda']['generic_name'].__len__() > 0:
		# 	returned_drugs[spl_id]['Generic Drug Name'] = drug['openfda']['generic_name'][0]
	




	return returned_drugs, brand, manufacturer, count
	

		# if 'indications_and_usage' in drug and drug['indications_and_usage'].__len__() > 0:
		# 	returned_drugs[spl_id]['indications_and_usage'] = drug['indications_and_usage'][0]
	
		# if 'how_supplied' in drug and drug['how_supplied'].count > 0:
		# 	returned_drugs[spl_id]['how_supplied'] = drug['how_supplied'][0]

		# if 'dosage_and_administration' in drug and drug['dosage_and_administration'].__len__() > 0:
		# 	returned_drugs[spl_id]'dosage_and_administration' = drug['dosage_and_administration'][0]

		# if 'description' in drug and drug['description'].__len__() > 0:		
		# 	returned_drugs[spl_id]['description'] = drug['description'][0]

		# if 'adverse_reactions' in drug and drug['adverse_reactions'].__len__() > 0:
		# 	returned_drugs[spl_id]['adverse_reactions'] = drug['adverse_reactions'][0]

		# if 'general_precautions' in drug and drug['general_precautions'].__len__() > 0:
		# 	returned_drugs[spl_id]['general_precautions'] = drug['general_precautions'][0]

		# if 'warnings' in drug and drug['warnings'].__len__() > 0:
		# 	returned_drugs[spl_id]['warnings'] = drug['warnings'][0]
	
	


		

		# all_drugs[requested_drug['spl_id']] = requested_drug

		# chaning vs referencing requested_drug... look up

		# db.session.add(drug)
		


	# print requested_drug



		# string = brand + ' by ' + manufacturer
		# brands_manufacturers.join(string)



# make a function called get drug, from this I want to 'store' 




