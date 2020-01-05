# -*- coding: utf-8 -*-
#!/usr/bin/python
import requests
import urllib
import json

api_key = '여러분의 API KEY'
refresh_token  = "여러분의 REFRESH KEY"
def getAccessToken(refreshToken) :
    url = "https://kauth.kakao.com/oauth/token"
    payload = "grant_type=refresh_token&client_id=%s&refresh_token="%(api_key) + refreshToken
    headers = {
        'Content-Type' : "application/x-www-form-urlencoded",
        'Cache-Control' : "no-cache",
    }
    reponse = requests.request("POST",url,data=payload, headers=headers)
    access_token = json.loads(((reponse.text).encode('utf-8')))
    print(access_token)
    return access_token


def sendText(accessToken, message) :
    url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'
    payload = '''template_object={
        "object_type" : "text",
        "text" :"%s",
        "link" : {
            "web_url" : "http://yourwebsite.for.pc",
            "mobile_web_url" : "http://yourwebsite.for.mobile"
        },
        "button_title" : "Visit"
        }'''%(message)
    payload = payload.encode('utf-8')
    print (payload)
    headers = {
        'Content-Type' : "application/x-www-form-urlencoded",
        'Cache-Control' : "no-cache",
        'Authorization' : "Bearer " + accessToken,
    }

    reponse = requests.request("POST",url,data=payload, headers=headers)
    access_token = json.loads(((reponse.text).encode('utf-8')))
    return access_token

result =  getAccessToken(refresh_token)   # 메세지 받을 사람의 REFRESH TOKEN 이용
if result['access_token'] is None:
    print ('access token get Error')
else:    
    print('access token:' + result['access_token'])
    ret = sendText(result['access_token'], 'Hello World  안녕')
    print (ret)