import requests
import random
import time

GATEWAY_URL = "http://localhost:5000/gateway"

while True:

    data = {
        "temperature": random.randint(20,35),
        "humidity": random.randint(40,70)
    }

    print("\nSensor sending:", data)

    requests.post(GATEWAY_URL, json=data)

    time.sleep(5)