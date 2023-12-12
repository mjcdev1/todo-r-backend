from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app, origins=['https://todo.mjc-dev.com'], methods=['POST'], supports_credentials=True)

# MongoDB connection setup
mongo_uri = "mongodb+srv://mjcdeveloper1:SmokingNarhwal226$@todo-r-cluster.nrtn6of.mongodb.net/?retryWrites=true&w=majority"
try:
    client = MongoClient(mongo_uri)
    db = client.data
    print("Connected to MongoDB successfully!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

# Your main route for handling POST requests
@app.route('/create_user', methods=['POST'])
def receive_data():
    try:
        data = request.get_json()
        lists = db.lists
        inserted_data = lists.insert_one(data)
        processed_data = "Received data: " + str(data)
        return processed_data, 200
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, threaded=True)

