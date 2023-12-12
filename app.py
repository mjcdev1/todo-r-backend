import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
from flask_cors import CORS

CORS(app, origins=['https://todo.mjc-dev.com'])


# MongoDB Atlas connection string
mongo_uri = "mongodb+srv://mjcdeveloper1:SmokingNarhwal226$@todo-r-cluster.nrtn6of.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongo_uri)
data = client.data 
lists = data.lists  # Move this outside of the route to avoid repeated database connections

@app.route('/create_list', methods=['POST'])
def create_list():
    try:
        received_data = request.get_json()
        inserted_data = lists.insert_one(received_data)  # Fix this line to insert received_data, not data
        processed_data = "Received data: " + str(received_data)
        
        # Add CORS headers to the response
        response = jsonify({"message": processed_data})
        response.headers.add("Access-Control-Allow-Origin", "https://todo.mjc-dev.com")
        
        return response, 200
    except Exception as e:
        return str(e), 500
