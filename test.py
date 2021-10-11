import requests
import json
headers = {
    'Content-Type': 'application/json',
}

body = { "tag": "text",
        "text": {"content": "Sent from AWS"}
        }

data = json.dumps(body)

response = requests.post('https://openapi.seatalk.io/webhook/group/YimMnwMARf6LBU6U-HKtWA', headers=headers, data=data)