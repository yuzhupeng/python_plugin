
import requests

url = "https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false"

data = {
    'first':'true',
    'pn':1,
    'kd':'python'
}

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36",
    "Referer":"https://www.lagou.com/jobs/list_python?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput="
}

response = requests.post(url,data=data,headers=headers)
# print(response.text)
print(type(response.text))       #<class 'str'>
print(type(response.json()))     #<class 'dict'>

print(response.json())           #获取为字典的形式