from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
# from model import connect_to_db, db, User, Route
# from text import send_text

app = Flask(__name__)


@app.route('/')
def index():

   """This is the page an org. or campaign sees after login. The organization can
   see their current stream of donations - visualized by tables/gallery style. The
   organization is able to send a text message to all users regarding stated goals."""

   return render_template('base.html')

if __name__ == "__main__":
	app = app.run(debug=True)