from flask import Flask, request, jsonify
import hashlib
from cryptography.fernet import Fernet

app = Flask(__name__)

# same key used in gateway
key = b'q7mFaCx0Bntl4gCUU0h-w-vcz7px7TRSg_EeXyyIvtw='
cipher = Fernet(key)

@app.route('/receive', methods=['POST'])
def receive_data():

    encrypted_data = request.json['data']
    received_hash = request.json['hash']

    # decrypt data
    decrypted = cipher.decrypt(encrypted_data.encode()).decode()

    # compute hash again
    calculated_hash = hashlib.sha256(decrypted.encode()).hexdigest()

    if calculated_hash == received_hash:
        status = "Integrity Verified"
    else:
        status = "Data Tampered!"

    print("\nCloud Received Data")
    print("Decrypted:", decrypted)
    print("Hash:", received_hash)
    print("Status:", status)

    return jsonify({"status": status})

if __name__ == '__main__':
    app.run(port=6000)