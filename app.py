from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/ping": {"origins": "*"}})

@app.route('/ping', methods=['POST', 'OPTIONS'])
def receive_ping():
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Methods': 'POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': 86400  # 24 hours
        }
        return '', 204, headers

    elif request.method == 'POST':
        try:
            data = request.get_json()

            print("Received data:", data)
            response_data = {'message': 'ping'}
            return jsonify(response_data), 200

        except Exception as e:
            # Handle any exceptions or errors
            print("Error:", str(e))
            return jsonify({'message': 'Internal server error'}), 500
    else:
        # If the request method is not POST or OPTIONS
        return jsonify({'message': 'Method not allowed'}), 405

if __name__ == '__main__':
    app.run(debug=True)
