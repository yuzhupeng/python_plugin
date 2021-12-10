import requests
import time
import random
import socket
import http.client
import re
from bs4 import BeautifulSoup
import sc.log4 
from lxml import etree

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










def getpagecontent(pageno,cookie):
    url='http://10.9.140.98/workflow_skc/apps/index.cfm?fuseaction=inquiryall.Apply'
    payload = 'CategoryID=3&BusinessModelAdminID=106&ApplyStatus=-100&ApplyerSection=-100&SApplyDate=&EApplyDate=&SCompleteDate=&ECompleteDate=&SDocApplyDate=&EDocApplyDate=&SDocCompleteDate=&EDocCompleteDate=&PageCount=100&PageNo={_PageNo}&SortKey=ApplyDate&Order=DESC&KeepSortKey=ApplyDate&AdminCD=&SAdminNumber=&EAdminNumber=&AdminCDNumber=&Subject1=&Subject2=&Subject3=&Subject4=&Subject5=&FreeWord=&Lst_ConditionParam=CategoryID%2CBusinessModelAdminID%2CApplyStatus%2CApplyerSection%2CSApplyDate%2CEApplyDate%2CSCompleteDate%2CECompleteDate%2CSDocApplyDate%2CEDocApplyDate%2CSDocCompleteDate%2CEDocCompleteDate%2CPageCount%2CPageNo%2CSortKey%2COrder%2CKeepSortKey%2CAdminCD%2CSAdminNumber%2CEAdminNumber%2CAdminCDNumber%2CSubject1%2CSubject2%2CSubject3%2CSubject4%2CSubject5%2CFreeWord'.format(_PageNo=pageno)
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
                    'Upgrade-Insecure-Requests': '1',
                    'cookie':cookie
                }
    # cookie=login()
    # cookie='CFID=4232877; CFTOKEN=81953532'
    response = requests.request("POST", url, headers=headers, data=payload)
    file = open('html.txt', 'a', encoding='utf-8')   
    data = response.text
 
    soup = BeautifulSoup(data, 'lxml')
    tables=soup.find_all('table')
    inv_info = []
    if len(tables)==0:
        return inv_info
  
    #table = soup.table;
    tr_arr = tables[1].find_all("tr");
    for tr in tr_arr:
        #//查询所有td
        tds = tr.find_all('td');  
        if len(tds)!=11:
            continue
        file.write('\n')
        file.write('--------------------')
        file.write('\n')
        # print(tds[1].text)
        temp = []
        for td in tds:
            if td.text.strip()=='目录' or td.text.strip()=='管理序号':
                break
            # print(td)
            # print(td.text)
            # print(td.find_all('a'))
            if len(td.text.strip())>0:
                file.write(td.text.strip())
                temp.append(td.text.strip())
            else:
                continue
            astr=td.find_all('a')
            if len(astr)>0:
            #    print(astr[0])
                file.write('\n')
                p1 = re.compile(r'[(](.*?)[)]', re.S) #最小匹配
                p2 = re.compile(r'[(](.*)[)]', re.S)  #贪婪匹配
                applyid=re.findall(p1, astr[0].attrs['href'])
                applyidno = applyid[0].replace('[','').replace(']','')
                temp.append(applyidno)
                file.write(applyidno)          
                #file.write(td.find_all('a'))
                file.write('\n')
        # file.write(tds)
            # print(tds);
                inv_info.append(temp)
        
    file.close()
    return inv_info
     
 
 
import pymssql 

#根据编号查询是否存在
def fecth_applyno(applyno):
    server = "."    # 连接服务器地址
    user = "sa" # 连接帐号
    password = "1"# 连接密码
    conn = pymssql.connect(server, user, password, "Skc_Business")  #获取连接
    cursor = conn.cursor() # 获取光标
    # 查询数据
    cursor.execute('SELECT count(*) FROM CasTravel WHERE BwfTravelNo=%s', applyno)
    # 遍历数据（存放到元组中） 方式1
    row = cursor.fetchone()
    if len(row)>1:
        conn.close()
        return True
    else:
        conn.close()
        return False
       
#插入cas用车申请单
def applydata_Update_Insert(inv_info):
    for info in inv_info:
        if len(info)>1:
          print (info[1])
          print (info[2])
          flags= fecth_applyno(info[1])
          if flags==True:
             print("执行更新")#执行更新
          else:
            get_apply_data(1,info[2],COO)
            print("执行插入")
#'CFID=4232877; CFTOKEN=81953532'

#BWF系统获取用车申请明细信息
def get_apply_data(pageno,applyids,cookie):
     url='http://10.9.140.98/workflow_skc/apps/index.cfm?fuseaction=inquiryall.ApplyDisp&ApplyID={applyid}'.format(applyid=applyids)
     payload = 'CategoryID=3&BusinessModelAdminID=106&ApplyStatus=-100&ApplyerSection=-100&SApplyDate=&EApplyDate=&SCompleteDate=&ECompleteDate=&SDocApplyDate=&EDocApplyDate=&SDocCompleteDate=&EDocCompleteDate=&PageCount=100&PageNo={_PageNo}&SortKey=ApplyDate&Order=DESC&KeepSortKey=ApplyDate&AdminCD=&SAdminNumber=&EAdminNumber=&AdminCDNumber=&Subject1=&Subject2=&Subject3=&Subject4=&Subject5=&FreeWord=&Lst_ConditionParam=CategoryID%2CBusinessModelAdminID%2CApplyStatus%2CApplyerSection%2CSApplyDate%2CEApplyDate%2CSCompleteDate%2CECompleteDate%2CSDocApplyDate%2CEDocApplyDate%2CSDocCompleteDate%2CEDocCompleteDate%2CPageCount%2CPageNo%2CSortKey%2COrder%2CKeepSortKey%2CAdminCD%2CSAdminNumber%2CEAdminNumber%2CAdminCDNumber%2CSubject1%2CSubject2%2CSubject3%2CSubject4%2CSubject5%2CFreeWord'.format(_PageNo=pageno)
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
                    'Upgrade-Insecure-Requests': '1',
                    'cookie':cookie
                }
    # cookie=login()
    # cookie='CFID=4232877; CFTOKEN=81953532'
     print(applyids)
     response = requests.request("POST", url, headers=headers, data=payload)
     
    #  soup = BeautifulSoup(response.text, 'lxml')
    #  tables=soup.find_all('table')
     
     
     try:
            html_text = response.content.decode("utf-8")
     except UnicodeDecodeError as e:
            print("解码api响应内容失败")
            return
     xphtml = etree.HTML(html_text)
     
     print(html_text)
     #/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr/td[4]/span/input
     #/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/span/input
     #/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[2]/td/table/tbody/tr[6]/td/table/tbody/tr/td[2]/span/input
     
      
   
      
     inputs = xphtml.xpath("//table")
     table2=inputs[5]
     vvv=table2.xpath("/tbody/tr[6]/td/table/tbody/tr/td[1]/span/input")
      
     detial=[]
     for li in inputs:
         values = li.xpath("@value")[0]
         if len(values)>1:
             detial.append(values)
     # xphtml = etree.HTML(html_text)
       
     
  
     print(xphtml)
     print(detial)


COO='CFID=4236026; CFTOKEN=79172508'
inv_info=getpagecontent(5,COO)
applydata_Update_Insert(inv_info)




for info in inv_info:
    if len(info)>1:
       print (info[1])
       print (info[2])
       for item in info:
           print(item)
 
 


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