import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# MongoDB Atlas connection string
mongo_uri = "mongodb+srv://mjcdeveloper1:SmokingNarhwal226$@todo-r-cluster.nrtn6of.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongo_uri)
data = client.data 
lists = data.lists  # Move this outside of the route to avoid repeated database connections

@app.route('/create_list', methods=['POST', 'OPTIONS'])
def create_list():
    try:
        received_data = request.get_json()

        if request.method == 'OPTIONS':
            # Handling CORS pre-flight request
            response = jsonify({'message': 'CORS pre-flight request successful'})
            response.headers['Access-Control-Allow-Origin'] = 'https://todo.mjc-dev.com'
            response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
            response.headers['Access-Control-Allow-Methods'] = 'POST'
            return response

        lists.insert_one(received_data)
        processed_data = "Received data: " + str(received_data)

        # Manual CORS headers for the actual request
        response = jsonify({"message": processed_data})
        response.headers['Access-Control-Allow-Origin'] = 'https://todo.mjc-dev.com'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        response.headers['Access-Control-Allow-Methods'] = 'POST'
        
        return response, 200
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    # For local development
    app.run(debug=True)
