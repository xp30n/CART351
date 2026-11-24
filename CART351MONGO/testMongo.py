from flask import Flask, render_template, request
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

# Sets a config variable
app.config["MONGO_URI"] = uri

mongo = PyMongo(app)

try:
    # Get the details of the client
    print(mongo.cx)
    
    # Get database
    print(mongo.db)
    
    # Get the collection
    print(mongo.db.plantRepo)
    
    print("You Successfully connected to MongoDB!")
    result = mongo.db.plantRepo.insert_one(
        {"testKeyMon" : "testValueMon"}
    )
    print(result)
except Exception as e:
    print(e)