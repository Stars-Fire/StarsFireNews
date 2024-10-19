from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['POST'])
def post_data():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400
    with open('received_data.json', 'w') as f:
        json.dump(data, f, indent=4)
    return jsonify({"message": "Data received and saved successfully"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=20230)