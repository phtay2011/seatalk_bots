import requests
import json
headers = {
    'Content-Type': 'application/json',
}

body = { "tag": "text",
        "text": {"content": "sample test test test",
                "mentioned_email_list": ['tianli.woon@seamoney.com','paul.tay@shopee.com']}
        }

data = json.dumps(body)

response = requests.post('https://openapi.seatalk.io/webhook/group/Tca0FDU9ToCHjqjhrzGENw', headers=headers, data=data)
