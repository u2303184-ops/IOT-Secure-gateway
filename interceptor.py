import requests

print("\nAttacker intercepting traffic...\n")

url = "http://localhost:6000/receive"

payload = {
    "data": "gAAAAABfakeEncryptedData123456",
    "hash": "123fakehash"
}

print("Captured Encrypted Packet:")
print(payload)