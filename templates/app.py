from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars")

@app.route ("/")
def index():
    mars_dict = {'news_title': news_title,'featured_img': featured_image, 'tweet': tweet, 'cerberus_img':cerberus_image, 'cerberus_title': cerberus_title, 'schiaparelli_image': schiaparelli_image, 'schiaparelli_title': schiaparelli_title, 'syrtis_img': syrtis_image, 'syrtis_title':syrtis_title, 'valles_img':valles_image, 'valles_title':valles_title}
    return render_template('index.html', dict=mars_dict)

@app.route ("/scrape")
def scrape():
    mars_data = scrape_mars.scrape_info

    mongo.db.collection.update({}, mars_data, upsert=True)

    return redirect("/")

if __name__ == '__main__':
    app.run(debug = True)
    
