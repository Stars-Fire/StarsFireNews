import requests
import json
from datetime import datetime

SERVER = "http://127.0.0.1:20230/postdata"

data = {
    "title": "test",
    "content": "man",
    "author": "TNTXZ",
    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "type": "test"
}
json_data = json.dumps(data)

try:
    response = requests.post(SERVER, json=data, headers={'Content-Type': 'application/json'})
    print("状态码:", response.status_code)
    print("返回值:", response.text)
except requests.exceptions.RequestException as e:
    print("Error:", e)