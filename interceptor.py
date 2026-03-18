from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

CLOUD_URL = "http://localhost:6000/receive"

@app.route('/intercept', methods=['POST'])
def intercept():

    data = request.json

    print("\n[INTERCEPTOR ACTIVE]")
    print("Captured Encrypted Packet:")
    print("Encrypted Data:", data['data'])
    print("Hash:", data['hash'])

    # Forward data to actual cloud
    response = requests.post(CLOUD_URL, json=data)

    return jsonify({"status": "Forwarded to cloud"})

if __name__ == '__main__':
    app.run(port=7000)