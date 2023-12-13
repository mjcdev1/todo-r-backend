from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api_test": {"origins": "*"}})  # Allow requests from any origin

@app.route('/api_test', methods=['POST'])
def handle_post_request():
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Process the data as needed
        # For demonstration purposes, just print the received data
        print("Received data:", data)

        # Return a success message
        return jsonify({'message': 'Request successful'}), 200

    except Exception as e:
        # Handle any exceptions or errors
        print("Error:", str(e))
        return jsonify({'message': 'Internal server error'}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
