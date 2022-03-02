import requests
import json
headers = {
    'Content-Type': 'application/json',
}

body = { "tag": "text",
        "text": {"content": "Test"}
        }

data = json.dumps(body)

response = requests.post('https://openapi.seatalk.io/webhook/group/JKbYxfWXRj2PlbqWCwJ9Jw', headers=headers, data=data)
