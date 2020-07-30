# Use Flask to render a template
# Use PyMongo to interact with our Mongo database
# Use the scraping code, we will convert from Jupyter notebook to Python.

from flask import Flask, render_template
from flask_pymongo import PyMongo
import scraping


# Connect to Mongo using PyMongo
app = Flask(__name__)
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


# Set Up App Routes
# Set up our Flask routes: 
# one for the main HTML page everyone will view when visiting the web app, 
# one to scrape new data

# Home page
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

# Scraping route
# This route will be the “button” of the web application, that scrapes updated data when we tell it to from the homepage of our web app
# It’ll be tied to a button that will run the code when it’s clicked
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return "Scraping Successful!"

# Tell Flask to run

if __name__ == "__main__":
   app.run()