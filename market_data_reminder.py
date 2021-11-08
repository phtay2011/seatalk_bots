import requests
import json
headers = {
    'Content-Type': 'application/json',
}

body = { "tag": "text",
        "text": {"content": "Dearest Nat, could i trouble you for the rates today, it will be of great help in my quest! FX Rates in by 3.55pm, the rest by 6.30pm -Sent from AWS ",
                "mentioned_email_list": ['natalie.huang@seamoney.com']}
        }
        
body2 = { "tag": "text",
        "text": {"content": "Dearest Nat, could i trouble you for the rates today, it will be of great help in my quest! FX Rates in by 3.55pm -Sent from AWS ",
                "mentioned_email_list": ['natalie.huang@seamoney.com']}
        }

data = json.dumps(body2)

response = requests.post('https://openapi.seatalk.io/webhook/group/YimMnwMARf6LBU6U-HKtWA', headers=headers, data=data)
