from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, Donor, Donation, Org, Campaign
# from text import send_text

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """This is the page an org. or campaign sees after login. The organization can
    see their current stream of donations - visualized by tables/gallery style. The
    organization is able to send a text message to all users regarding stated goals."""

    return render_template('homepage.html')


@app.route('/donor_landing', methods=['GET'])
def show_donor_landing():
    """This will route the donor to the donor landing page"""
    
    return render_template('donor_landing.html')


@app.route('/org_landing', methods=['GET', 'POST'])
def show_org_land():
    org_name = Org.query.filter_by(org_name='The Org').first()
    campaign = Campaign.query.filter_by(name='Coding for Kids').first()
    return render_template('org_landing.html', org_name=org_name, campaign1=campaign1, campaign2=campaign2, campaign3=campaign3)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
 
    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()