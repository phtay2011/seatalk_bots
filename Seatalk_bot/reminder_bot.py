import requests
import json
headers = {
    'Content-Type': 'application/json',
}

body = { "tag": "text",
        "text": {"content": "Please check 1) SG TMS Dev and UAT Analytics Server, 2) ID TMS Dev Analytics Server and delete old backup files. We only need the latest 3 backup files",
                "mentioned_email_list": ['tianli.woon@seamoney.com','paul.tay@shopee.com']}
        }

data = json.dumps(body)

response = requests.post('https://openapi.seatalk.io/webhook/group/vQ_sH0dzRiOoya-f6oi7Ew', headers=headers, data=data)
