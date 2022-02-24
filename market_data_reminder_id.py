import requests
import json
headers = {
    'Content-Type': 'application/json',
}
body3 = { "tag": "text",
        "text": {"content": "1) Jake to to refresh this file for today. 2) Fiona to manual upload the sec prices once Jake refreshed",
                "mentioned_email_list": ['jake.wen@seamoney.com','fiona.coa@seabank.co.id']}
        }


data3 = json.dumps(body3)
response3 = requests.post('https://openapi.seatalk.io/webhook/group/RxP3Cg97TRmIyzafYVW6KQ', headers=headers, data=data3)