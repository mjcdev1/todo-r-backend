import os, requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app, origins=['https://wordgame.mjc-dev.com', 'https://admin.mjc-dev.com'])

# MongoDB Atlas connection string
mongo_uri = "mongodb+srv://mjcunn:NecroticUvula1$@cluster0.zwacvys.mongodb.net/mydatabase?retryWrites=true&w=majority"

# Create a MongoClient instance
client = MongoClient(mongo_uri)

# Access the MongoDB database
db = client.users  
db_game = client.game

@app.route('/create_user', methods=['POST'])
def receive_data():
    try:
        data = request.get_json()

        threes_user_data = db.threes_user_data
        fours_user_data = db.fours_user_data
        fives_user_data = db.fives_user_data
        sixes_user_data = db.sixes_user_data
        fives_user_data_monthly = db.fives_user_data_monthly

        inserted_data = threes_user_data.insert_one(data)
        inserted_data = fours_user_data.insert_one(data)
        inserted_data = fives_user_data.insert_one(data)
        inserted_data = sixes_user_data.insert_one(data)
        inserted_data = fives_user_data_monthly.insert_one(data)
        
        processed_data = "Received data: " + str(data)
        
        return processed_data, 200
    except Exception as e:
        return str(e), 500
