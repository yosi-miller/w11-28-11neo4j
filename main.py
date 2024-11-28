# The application will send the JSON to the address: http://localhost:5000/api/phone_tracker
# Create your own Flask application that will handle requests to the above address.
import json

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/phone_tracker', methods=['POST'])
def phone_tracker():
    data = request.json
    print(data)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)