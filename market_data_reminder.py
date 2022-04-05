import requests
import json
headers = {
    'Content-Type': 'application/json',
}

body = { "tag": "text",
        "text": {"content": "Hi Nat/Kah Lun, kindly refresh the rate files for today. FX Rates in by 3.55pm, the rest by 6.30pm -Sent from AWS ",
                "mentioned_email_list": ['natalie.huang@seamoney.com','kahlun.leong@maribank.com.sg']}
        }

data = json.dumps(body)
response = requests.post('https://openapi.seatalk.io/webhook/group/rtNj3dDVQG6SWLCSmOncGA', headers=headers, data=data)
