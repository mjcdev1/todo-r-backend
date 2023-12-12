import os, requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app, origins=['https://wordgame.mjc-dev.com', 'https://admin.mjc-dev.com'])

# MongoDB Atlas connection string
mongo_uri = "mongodb://atlas-sql-6578acceabdc1124b04cb8d2-l1dlm.a.query.mongodb.net/data?ssl=true&authSource=admin"
client = MongoClient(mongo_uri)

data = client.data 

@app.route('/create_list', methods=['POST'])
def create_list():
    try:
        received_data = request.get_json()

        lists = data.lists

        inserted_data = lists.insert_one(data)
        
        processed_data = "Received data: " + str(received_data)
        
        return processed_data, 200
    except Exception as e:
        return str(e), 500
