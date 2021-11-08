import requests
import json
headers = {
    'Content-Type': 'application/json',
}

body = { "tag": "text",
        "text": {"content": "Hi all, today is 8 Nov, will start work again. Daily reminders will be sent at 14:50 and 18:00. As as UAT 1"}
        }
        
data = json.dumps(body)

response = requests.post('https://openapi.seatalk.io/webhook/group/YimMnwMARf6LBU6U-HKtWA', headers=headers, data=data)