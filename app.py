from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin
from pymongo import MongoClient
import os

app = Flask(__name__)

mongo_uri = "mongodb+srv://mjcdeveloper1:NecroticUvula@todo-r-cluster.nrtn6of.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongo_uri)
db = client.data

@app.route('/create_user', methods=['POST', 'OPTIONS'])
@cross_origin(origin='https://todo.mjc-dev.com', methods=['POST'], headers=['Content-Type'])
def receive_data():
    if request.method == 'OPTIONS':
        response = make_response()
        return response

    try:
        data = request.get_json()
        lists = db.lists
        inserted_data = lists.insert_one(data)
        processed_data = "Received data: " + str(data)

        response = make_response(processed_data, 200)
        return response

    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, threaded=True)

