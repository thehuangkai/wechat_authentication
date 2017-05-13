import json
import time
import requests
import string
import urllib

appid = 'xxx'
appsecret = 'xxx'
token_url = """https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s"""
getUrl = token_url % (appid, appsecret)
res = requests.get(getUrl)
access_token = res.json()['access_token']


postUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token="+access_token
data ="""
    {
        "button":
        [
            {
                "type": "click",
                "name": "button 1",
                "key":  "mpGuide"
            },
            {
                "name": "button 2",
                "sub_button":
                [
                    {
                        "type": "view",
                        "name": "button 3",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
                    },
                    {
                        "type": "view",
                        "name": "button 4",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
                    },
                    {
                        "type": "view",
                        "name": "button 5",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1433747234&token=&lang=zh_CN"
                    }
                ]
            },
          ]
    }
    """
data=data.encode('utf-8')

headers = {'Content-Type': 'application/json'}
res2 = requests.post(postUrl, data, headers=headers)
print(res2.json())
