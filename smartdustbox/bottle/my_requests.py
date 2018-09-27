# coding utf-8

import requests
import json
import time
import datetime


# url = 'https://example.com/'
url  = "http://192.168.0.4:8080/setLed"

# response = requests.get(url)
# response = requests.post(url)

cnt = 0
while True:
    time.sleep(0.01)

    cnt += 1
    # payload = {"yaw": "okinawa", "pitch": "okinawa", "roll": "okinawa", "slider": "okinawa"}
    payload = {"yaw": 1, "pitch": 2, "roll": 3, "slider": cnt}

    # response = requests.post(url, data=json.dumps(payload))
    response = requests.post(url, json=payload)


    print(response)
    # <Response [200]>

    print(type(response))
    # <class 'requests.models.Response'>
