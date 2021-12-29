import requests
import json

# Reminder for PM to check Regression defects daily
headers = {
    'Content-Type': 'application/json',
}

body = { "tag": "text",
        "text": {"content": "Hi, remember to check regression defects. Here is the link to the template - https://docs.google.com/spreadsheets/d/1JNW15sy608B9YXPwNS5auLa67IIhg5MN/edit#gid=1061813672",
                "at_all": True
        }
        }

data = json.dumps(body)

response = requests.post('https://openapi.seatalk.io/webhook/group/vQ_sH0dzRiOoya-f6oi7Ew', headers=headers, data=data)
