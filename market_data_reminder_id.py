import requests
import json
headers = {
    'Content-Type': 'application/json',
}
body3 = { "tag": "text",
        "text": {"content": "can help to refresh this file for today?",
                "mentioned_email_list": ['jake.wen@seamoney.com']}
        }


data3 = json.dumps(body3)
response3 = requests.post('https://openapi.seatalk.io/webhook/group/RxP3Cg97TRmIyzafYVW6KQ', headers=headers, data=data3)