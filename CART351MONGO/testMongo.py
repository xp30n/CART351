from flask import Flask, render_template, request, redirect, url_for, session
from flask_pymongo import PyMongo

from dotenv import load_dotenv
import os

load_dotenv()

db_user = os.getenv('MONGODB_USERNAME')
db_pass = os.getenv('MONGODB_PASSWORD')
db_name = os.getenv('DATABASE_NAME')

print(db_user)

uri = os.getenv("MONGODB_URI")
uri = uri + f"/{db_name}?retryWrites=true&w=majority"

app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'

# Sets a config variable
app.config["MONGO_URI"] = uri

mongo = PyMongo(app)

# try:
#     # Get the details of the client
#     print(mongo.cx)
    
#     # Get database
#     print(mongo.db)
    
#     # Get the collection
#     print(mongo.db.plantRepo)
    
#     print("You Successfully connected to MongoDB!")
#     result = mongo.db.plantRepo.insert_one(
#         {"testKeyMon" : "testValueMon"}
#     )
#     print(result)
# except Exception as e:
#     print(e)
    
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/insertTestPage")
def insertTest():
    session.pop('ids', default=None)
    return render_template("testInsert.html")

@app.route("/insertMany")
def insertMany():
    data = [
        {
            'owner_name': 'Sarah',
            'plant_name': 'Snake Plant',
            'birthDate': '2002-06-12',
            'geoLoc': 'Montreal',
            'descript': 'Description for the plant',
            'imagePath': 'images/one.png'
        },
        {
            'owner_name': 'Sarah',
            'plant_name': 'Cactus',
            'birthDate': '2005-06-13',
            'geoLoc': 'Toronto',
            'descript': 'Description for the plant',
            'imagePath': 'images/seven.png'
        },
        {
            'owner_name': 'Sarah',
            'plant_name': 'Agapanthus',
            'birthDate': '2003-03-19',
            'geoLoc': 'Halifax',
            'descript': 'Description for the plant',
            'imagePath': 'images/seventeen.png'
        },
        {
            'owner_name': 'Stephen',
            'plant_name': 'Baby Rubber Plant',
            'birthDate ': '1999-07-18',
            'geoLoc': 'Edinborough',
            'descript': 'Description for the plant',
            'imagePath': 'images/ten.png'
        },
        {
            'owner_name': 'Stephen',
            'plant_name': 'Dahlia',
            'birthDate': '2000-05-06',
            'geoLoc': 'London',
            'descript': 'Description for the plant',
            'imagePath': 'images/thirteen.png'
        },
        {
            'owner_name': 'Harold',
            'plant_name': 'Daphne',
            'birthDate': '2012-10-21',
            'geoLoc': 'New York',
            'descript': 'Description for the plant',
            'imagePath': 'images/three.png'
        },
        {
            'owner_name': 'Martha',
            'plant_name': 'Daylily',
            'birthDate': '2017-08-21',
            'geoLoc': 'Paris',
            'descript': 'Description for the plant',
            'imagePath': 'images/nine.png'
        }
    ]
    
    try:
        # Insert many works
        result = mongo.db.plantRepo.insert_many(data)
        session['ids'] = result.inserted_ids
        return redirect(url_for('testIds'))
    except Exception as e:
        print(e)
        
        
@app.route("/testIds")
def testIds():
    print(session['ids'])
    return render_template("testIds.html")

@app.route("/viewResults")
def viewResults():
    result = mongo.db.plantRepo.find()
    print(result)
    
    return render_template("viewResults.html", result=result)

@app.route("/updateOne")
def updateOne():
    try:
        updatedRepoItem = mongo.db.plantRepo.find_one_and_update(
            {'plant_name' : 'Agapanthus'},
            {'$set' : {'descript' : 'a more precise description'}}
        )
        return redirect(url_for("insertTest"))
    except Exception as e:
        print(e)
    
app.run(debug=True)