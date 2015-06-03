# from server import app
import requests
import json

from model import connect_to_db, User, db, Drug

f = open("secrets.txt")
keys = f.read().strip().split()
openfda_api_key = keys[0]




def search_openfda_by_spl_id(spl_set_id):
    
    r = requests.get('https://api.fda.gov/drug/label.json?api_key=%s&search=set_id:%s&limit=100' % (openfda_api_key, spl_set_id)).json()
    print 'https://api.fda.gov/drug/label.json?api_key=%s&search=set_id:%s&limit=100' % (openfda_api_key, spl_set_id)

    druglist = r['results']
    print ("*")*30
    

    
    for drug in druglist:
        print "\n\n"
        # print drug
        drugdict = {}

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
                drugdict[x] = drug[x][0]
            else:
                drugdict[x] = "info not provided by mfg"


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
                drugdict[x] = drug['openfda'][x][0]
            else:
                drugdict[x] = "info not provided by mfg"



    # manufacturer_name = 'manufacturer_name' in drug ? drug['manufacturer_name'] : "info not provided by mfg"
    # product_type = drugdata['product_type']
    # description = drugdata['description']
    # dosage_and_administration = drugdata['dosage_and_administration']
    # route = drugdata['route']
    # generic_name = drugdata['generic_name']
    # brand_name = drugdata['brand_name']
    # substance_name = drugdata['substance_name']
    # product_ndc = drugdata['product_ndc']
    # adverse_reactions = drugdata['adverse_reactions']
    # how_supplied = drugdata['how_supplied']
    # indications_and_usage = drugdata['indications_and_usage']

    new_drug = Drug(manufacturer_name=drugdict['manufacturer_name'], 
                    product_type=drugdict['product_type'],
                    description=drugdict['description'],
                    dosage_and_administration=drugdict['dosage_and_administration'],
                    route=drugdict['route'], 
                    generic_name=drugdict['generic_name'], 
                    brand_name=drugdict['brand_name'], 
                    substance_name=drugdict['substance_name'], 
                    product_ndc=drugdict['product_ndc'], 
                    adverse_reactions=drugdict['adverse_reactions'], 
                    how_supplied=drugdict['how_supplied'], 
                    indications_and_usage=drugdict['indications_and_usage'], 
                    spl_set_id=drugdict['spl_set_id'])


    db.session.add(new_drug)
    db.session.commit()

