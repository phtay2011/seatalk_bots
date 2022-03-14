import requests
import json
headers = {
    'Content-Type': 'application/json',
}

body = { "tag": "text",
        "text": {"content": "Test"}
        }

data = json.dumps(body)

response = requests.post('https://openapi.seatalk.io/webhook/group/zPJjSBydR3yJXfERJ6qznw', headers=headers, data=data)
