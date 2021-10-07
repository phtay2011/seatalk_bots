#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 15:24:28 2021

@author: paul.tay
"""
import requests
import json
headers = {
    'Content-Type': 'application/json',
}

body = { "tag": "text",
        "text": {"content": "Hi, remember to check that all the rates are in qtm by 6.30pm. Rates include: 1)FX & FSP, 2) Swaps, 3) Deposit, 4) Bonds",
                "mentioned_email_list": ['tianli.woon@seamoney.com']}
        }

data = json.dumps(body)

response = requests.post('https://openapi.seatalk.io/webhook/group/YimMnwMARf6LBU6U-HKtWA', headers=headers, data=data)


