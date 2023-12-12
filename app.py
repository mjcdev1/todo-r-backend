from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app, origins=['https://todo.mjc-dev.com', 'https://todo-r-backend-97c32160812e.herokuapp.com'])



mongo_uri = "mongodb+srv://mjcdeveloper1:NecroticUvula@todo-r-cluster.nrtn6of.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(mongo_uri)
db = client.data

@app.route('/create_user', methods=['POST', 'OPTIONS'])
def receive_data():
    if request.method == 'OPTIONS':
        return jsonify(), 200  # Respond to the preflight request
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

