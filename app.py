from flask import Flask, request, jsonify, make_response
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
        response = make_response()
        response.headers.add('Access-Control-Allow-Origin', 'https://todo.mjc-dev.com')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response, 200  # Respond to the preflight request

    try:
        data = request.get_json()
        lists = db.lists
        inserted_data = lists.insert_one(data)
        processed_data = "Received data: " + str(data)

        response = make_response(processed_data, 200)
        response.headers.add('Access-Control-Allow-Origin', 'https://todo.mjc-dev.com')
        return response

    except Exception as e:
        return str(e), 500


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, threaded=True)

