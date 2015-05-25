"""medme"""

# from jinja2 import StrictUndefined
# import search_openFDA import seed_drugs seeds_drugs.variable name 
from flask import Flask, render_template, request
from search_openfda import search_openfda
import requests

 # session, redirect

from model import connect_to_db, User, db
# from search_openFDA import 

app = Flask(__name__)
app.secret_key = "ABC"

# app.jinja_env.undefined = StrictUndefined

@app.route("/")
def index():
	"""Homepage and search"""

	return render_template("homepage.html")

@app.route("/drug_search_results", methods=['POST'])
#if you land on /drug_seearch resutls from a post request, do this search 
def search():
	"""User inputs drug search here"""
	
	keywords = request.form["drugname_keywords"]

	alldrugresults, count = search_openfda(keywords)


	return render_template("drug_search_results.html", alldrugresults = alldrugresults, count = count )




# @app.route("/drug_results", methods=['POST'])
# def get_results():
# 	pass


if __name__ == "__main__":

    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension

    # Do not debug for demo
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbarExtension(app)
#
    app.run()