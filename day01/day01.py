import requests
import json

base_url = "http://shop-xo.hctestedu.com/index.php"
# 题目一:注册
reg_params ={
    "s":"/index/user/reg",
    "application":"app",
    "application_client_type":"weixin"
}
headers = {
    'Content-Type': 'multipart/form-data',
    'X-Requested-With': 'XMLHttpRequest'
}
data = {
    "accounts": "jiji03",
    "pwd": 123456,
    "type": "username"
}
# reg_res = requests.post(url=base_url,params=reg_params, headers=headers, data=data).json()
# print("============注册成功============")
# print(reg_res)

#题目二:登入token
log_params ={
    "s":"/index/user/login",
    "application":"app",
    "application_client_type":"weixin"
}
log_res = requests.post(url=base_url,params=log_params, headers=headers, data=data).json()
# print(log_res)
token=log_res['data']['token']
print("============登入的token============")
print(token)
# token=jsonpath.jsonpath(log_res.json(),"$..token")


# #题目三:我的消息列表
mes_params ={
    "s":"api/message/index",
    "application":"app",
    "application_client_type":"weixin",
    "token":token
}
mes_headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest'
}
mes_data = {
    "page":1
}
mes_res = requests.post(url=base_url,params=mes_params, headers=mes_headers, data=mes_data).json()
print("============我的消息列表============")
print(mes_res)