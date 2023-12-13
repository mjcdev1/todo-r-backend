from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://10.0.0.187:8080"])

@app.route('/ping', methods=['POST'])
def receive_ping():
    if request.method == 'POST':
        try:
            data = request.get_json()
            print("Received data:", data)
            response_data = {'message': 'ping'}
            return jsonify(response_data), 200

        except Exception as e:
            print("Error:", str(e))
            return jsonify({'message': 'Internal server error'}), 500
    else:
        return jsonify({'message': 'Method not allowed'}), 405

if __name__ == '__main__':
    app.run(debug=True)
