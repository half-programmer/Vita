# -*- coding:utf-8 -*-


import sys, urllib, urllib2, json
url = "http://imlaixin.cn/Api/send/data/json?accesskey=5025&secretkey=754c1c14fdda4935c127af9d9331447ed752de97&mobile=15151861978&content=尊敬的用户您好，您的验证码为：1234，请不要告诉别人哦！【Vita】"
req = urllib2.Request(url)
resp = urllib2.urlopen(req)
str = resp.read()
if(str):
    print(str)