from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ping', methods=['POST'])
def receive_ping():
    if request.method == 'POST':
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
        # If the request method is not POST
        return jsonify({'message': 'Method not allowed'}), 405

if __name__ == '__main__':
    app.run(debug=True)
