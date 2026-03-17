from flask import Flask, request, jsonify
import hashlib
import requests
from cryptography.fernet import Fernet

app = Flask(__name__)

# AES key
key = b'q7mFaCx0Bntl4gCUU0h-w-vcz7px7TRSg_EeXyyIvtw='
cipher = Fernet(key)

print("Gateway AES Key:", key)

CLOUD_URL = "http://localhost:6000/receive"

@app.route('/gateway', methods=['POST'])
def gateway():

    data = request.json
    message = str(data)

    print("\nGateway received sensor data:", message)

    # SHA256 hash
    hash_value = hashlib.sha256(message.encode()).hexdigest()

    # AES encryption
    encrypted = cipher.encrypt(message.encode())

    print("\n--- Data Leaving Gateway ---")
    print("Encrypted Payload:", encrypted.decode())
    print("Hash:", hash_value)
    print("----------------------------")

    print("Encrypted Data:", encrypted.decode())
    print("Hash:", hash_value)

    payload = {
        "data": encrypted.decode(),
        "hash": hash_value
    }

    # send to cloud
    response = requests.post(CLOUD_URL, json=payload)

    return jsonify({"message": "Data secured and sent to cloud"})

if __name__ == '__main__':
    app.run(port=5000)