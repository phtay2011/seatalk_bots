import requests
import json
headers = {
    'Content-Type': 'application/json',
}

body = { "tag": "text",
        "text": {"content": "Hi Nat/Kah Lun, kindly refresh the rate files for today. FX Rates in by 3.55pm, the rest by 6.30pm -Sent from AWS ",
                "mentioned_email_list": ['natalie.huang@seamoney.com'],['kahlun.leong@maribank.com.sg']}
        }

body2 = { "tag": "text",
        "text": {"content": "Dearest Nat, could i trouble you for the rates today, it will be of great help in my quest! FX Rates in by 3.55pm -Sent from AWS ",
                "mentioned_email_list": ['natalie.huang@seamoney.com']}
        }


body3 = { "tag": "text",
        "text": {"content": "[TEST] Selamat pagi Jake! could i trouble you for the rates today. All Rates in by 6.30pm",
                "mentioned_email_list": ['jake.wen@seamoney.com']}
        }

data = json.dumps(body)

response = requests.post('https://openapi.seatalk.io/webhook/group/rtNj3dDVQG6SWLCSmOncGA', headers=headers, data=data)

data3 = json.dumps(body3)
#response3 = requests.post('https://openapi.seatalk.io/webhook/group/RxP3Cg97TRmIyzafYVW6KQ', headers=headers, data=data3)
