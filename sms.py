# -*- coding: utf-8 -*-
import sys, json
from urllib import request

def format_url():
    url = ('http://apis.baidu.com/sms_net/sms_net_sdk/sms_net_sdk'
           '?content=%E7%9F%AD%E4%BF%A1%E7%9F%AD%E4%BF%A1%E6%8E%A5%E5%8F%A3%E9%AA%8C%E8%AF%81%E7%A0%811111'
           '&mobile=13685795128')
    return url

url = format_url()
req = request.Request(url)
req.add_header("apikey", "1f0a62a2d")

site = request.urlopen(req)
response_byte = site.read()
response = response_byte.decode('utf8')
if(response):
    print(response)