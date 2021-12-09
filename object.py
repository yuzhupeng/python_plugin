import requests
import time
import random
import socket
import http.client
import re
from bs4 import BeautifulSoup
import sc.log4 


log = sc.log4.get_logger()

def getContent(url,header=None,datas = None,cookie=None):
    _header=''
    if header==None:     
     _header={
       'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36', #模拟登陆的浏览器
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,fil;q=0.7,zh-TW;q=0.6',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host':'10.9.140.98',
                'Origin':'http://10.9.140.98',
                'Referer': 'http://10.9.140.98/workflow_skc/logon/index.cfm',
                'Upgrade-Insecure-Requests': '1'
    } # request 的请求头
    else:
       _header= header
    
    
    timeout = random.choice(range(80, 180))
    while True:
        try:
            rep = requests.request("POST",url,headers = _header,data=datas,timeout = timeout,cookies=cookie) #请求url地址，获得返回 response 信息
            rep.encoding = 'utf-8'
            break
        except socket.timeout as e: # 以下都是异常处理
            log.error( '3:', e)
            time.sleep(random.choice(range(8,15)))

        except socket.error as e:
            log.error( '4:', e)
            time.sleep(random.choice(range(20, 60)))

        except http.client.BadStatusLine as e:
            log.error( '5:', e)
            time.sleep(random.choice(range(30, 80)))

        except http.client.IncompleteRead as e:
            log.error( '6:', e)
            time.sleep(random.choice(range(5, 15)))
    log.info('request success')
    return rep # 返回的 Html 全文

def login():
    LOGIN_URL = 'http://10.9.140.98/workflow_skc/logon/index.cfm?fuseaction=logon'  #请求的URL地址
    DATA = {"UserName":'0306081',"Password":'skc0306081'}   #登录系统的账号密码,也是我们请求数据

    HEADERS = { 
                'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36', #模拟登陆的浏览器
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,fil;q=0.7,zh-TW;q=0.6',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host':'10.9.140.98',
                'Origin':'http://10.9.140.98',
                'Referer': 'http://10.9.140.98/workflow_skc/logon/index.cfm',
                'Upgrade-Insecure-Requests': '1'
            }
    RES = getContent(LOGIN_URL,datas=DATA,header=HEADERS)  #模拟登陆操作 获取cookie
    # print (RES.text) #打印返回的文本信息
    # print(RES.cookies) 
    return RES.cookies











url='http://10.9.140.98/workflow_skc/apps/index.cfm?fuseaction=inquiryall.Apply'
payload = 'DispType=1&PageCount=100&AdminCD=&SAdminNumber=&EAdminNumber=&AdminCDNumber=&CategoryID=3&BusinessModelAdminID=106&FreeWord=&ApplyerSection=-100&ApplyStatus=-100&Subject1=&Subject2=&Subject3=&Subject4=&Subject5=&SApplyDate=&EApplyDate=&SDocApplyDate=&EDocApplyDate=&SCompleteDate=&ECompleteDate=&SDocCompleteDate=&EDocCompleteDate=&SubBtn=%E8%A1%A8%E7%A4%BA'
headers = {
                'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36', #模拟登陆的浏览器
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,fil;q=0.7,zh-TW;q=0.6',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host':'10.9.140.98',
                'Origin':'http://10.9.140.98',
                'Referer': 'http://10.9.140.98/workflow_skc/apps/index.cfm?fuseaction=inquiryall',
                'Upgrade-Insecure-Requests': '1'
            }


cookie=login()
response = requests.request("POST", url, headers=headers, data=payload,cookies=cookie)
 

file = open('html.txt', 'a', encoding='utf-8')
 
 
 

data = response.text
   # print (RES.text) #打印返回的文本信息
   # print(RES.cookies) 
# print(data)
soup = BeautifulSoup(data, 'lxml')
tables=soup.find_all('table')

#table = soup.table;
tr_arr = tables[1].find_all("tr");
for tr in tr_arr:
    #//查询所有td
    tds = tr.find_all('td');
    if len(tds)!=11:
        continue
    for td in tds:
        print(td)
        print(td.text)
        print(td.find_all('a'))
        file.write(td.text)
        astr=td.find_all('a')
        if len(astr)>0:
           print(astr[0])
           file.write(astr[0].text)
        #file.write(td.find_all('a'))
        file.write('----------------------')
    # file.write(tds)
        print(tds);

file.close()
 












import json

my_dict = {
    'name': '骆昊',
    'age': 40,
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}


print(my_dict)
print('-------------------')
print(json.dumps(my_dict))