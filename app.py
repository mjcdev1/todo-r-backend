from flask import Flask, request, jsonify

app = Flask(__name__)

# CORS middleware
@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    return response

# Your API endpoint
@app.route('/api_test', methods=['POST', 'OPTIONS'])
def handle_post_request():
    if request.method == 'OPTIONS':
        return '', 200  # Respond successfully to preflight request

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


