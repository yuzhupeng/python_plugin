import requests
import time
import random
import socket
import http.client
import re
from bs4 import BeautifulSoup
import sc.log4 
from lxml import etree
import json
import pymssql 

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
    # file = open('html.txt', 'a', encoding='utf-8')   
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
        if len(tds)!=11 or tds[0].text.strip()=='目录'or tds[0].text.strip()=='管理序号':
            continue
        temp = []
        
        if tds[0].text.strip()=='目录' or tds[0].text.strip()=='管理序号':
                break
        if  len(tds[1].text.strip())>0:
             temp.append(tds[1].text.strip())
        else:
             continue
        astr=tds[1].find_all('a')
         
        if len(astr)>0:
                p1 = re.compile(r'[(](.*?)[)]', re.S) #最小匹配
                p2 = re.compile(r'[(](.*)[)]', re.S)  #贪婪匹配
                applyid=re.findall(p1, astr[0].attrs['href'])
                applyidno = applyid[0].replace('[','').replace(']','')
                temp.append(applyidno)
                
        temp.append(tds[5].text.strip())
        inv_info.append(temp)
         
       
       
       
        # for td in tds:
        #     if td.text.strip()=='目录' or td.text.strip()=='管理序号':
        #         break
            
        #     if len(td.text.strip())>0:
        #         temp.append(td.text.strip())
        #     else:
        #         continue
        #     astr=td.find_all('a')
        #     if len(astr)>0:
        #         p1 = re.compile(r'[(](.*?)[)]', re.S) #最小匹配
        #         p2 = re.compile(r'[(](.*)[)]', re.S)  #贪婪匹配
        #         applyid=re.findall(p1, astr[0].attrs['href'])
        #         applyidno = applyid[0].replace('[','').replace(']','')
        #         temp.append(applyidno)
     
        #         inv_info.append(temp)
 
    return inv_info
     
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
    applyformlist=[]
    for info in inv_info:
        if len(info)>1:
          print (info[1])
          print (info[2])
          flags= fecth_applyno(info[0])
          if flags==True or info[2]=='取消' or info[2]=='退回':
             print("执行更新")#执行更新
          else:
            detial=get_apply_data(1,info[1],COO,info[0])
            time.sleep(2)
            if len(detial)>0:
               print(f'获取【{info[1]}】的数据完成！')
               applyformlist.append(detial)
               file = open('html.txt', 'a', encoding='utf-8') 
               js = json.dumps(detial,ensure_ascii=False)
               file.write(js+'\n')
               file.write('---------------'+'\n')
               file.close()  #关闭
            else:
                print(f'获取【{info[1]}】的数据失败！')
            
    return applyformlist
#'CFID=4232877; CFTOKEN=81953532'

#BWF系统获取用车申请明细信息
def get_apply_data(pageno,applyids,cookie,applyno):
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
     
     #print(html_text)
     #/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr/td[4]/span/input
     #/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/span/input
     #/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[2]/td/table/tbody/tr[6]/td/table/tbody/tr/td[2]/span/input
     #/html/body/table[2]/tr/td/form/table[1]/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr/td[2]/span/textarea
     #/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr/td[4]/span/input
     #/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[2]/td/table/tbody/tr[6]/td/table/tbody/tr/td[2]/span/input
     #/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[2]/td/table/tbody/tr[7]/td/table/tbody/tr/td[2]/span/input
     #/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[2]/td/table/tbody/tr[8]/td/table/tbody/tr/td[2]/span/input  联系人手机  
     #/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[2]/td/table/tbody/tr[8]/td/table/tbody/tr/td[6]/span/input 经费代码
     #/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[2]/td/table/tbody/tr[8]/td/table/tbody/tr/td[4]/span/input
     #/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[2]/td/table/tbody/tr[15]/td/table/tbody/tr[5]/td[2]/span
     #/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[2]/td/table/tbody/tr[15]/td/table/tbody/tr[6]/td[2]/span
     #html/body/table[3]/tbody/tr/td/form/table[1]/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr/td[2]/span/textarea
     inputs = xphtml.xpath("//table")
     table2=inputs[5]
     ins=table2.xpath("./tr[1]/td/table/tr") 
     insv=table2.xpath("./tr[1]/td/table/tr/td[1]")
     applytpye=table2.xpath("./tr[1]/td/table/tr/td[2]/span/textarea")[0].text#申请用车类型 
     reason=table2.xpath("./tr[1]/td/table/tr/td[4]/span/input")[0].get('value', default=None)#变更、取消理由
     usereason=table2.xpath("./tr[6]/td/table/tr/td[2]/span/input")[0].get('value', default=None)#用车理由
     DetailedAddres=table2.xpath("./tr[7]/td/table/tr/td[2]/span/input")[0].get('value', default=None)#行程详细地址
     PhonePassenger=table2.xpath("./tr[8]/td/table/tr/td[2]/span/input")[0].get('value', default=None)#联系人手机
     ShareCore=table2.xpath("./tr[8]/td/table/tr/td[6]/span/input")[0].get('value', default=None)#经费代码
     CostDepartment=table2.xpath("./tr[8]/td/table/tr/td[4]/span/input")[0].get('value', default=None)#部门
     applyperson=table2.xpath("./tr[15]/td/table/tr[5]/td[2]/span")[0].text#申请人
     applydate=table2.xpath("./tr[15]/td/table/tr[6]/td[2]/span")[0].text#申请日期
     applyform= {'applyno':applyno,'applytype':applytpye,'reason':reason,'userason':usereason,'DetailedAddress':DetailedAddres,
      'PhonePassenger':PhonePassenger,'ShareCore':ShareCore,'CostDepartment':CostDepartment,'applyperson':applyperson,'applydate':applydate
      }
     detial=[]
     detial.append(applyform)
      #经费负担部门
     return applyform
    

COO='CFID=4238286; CFTOKEN=15557770'
inv_info=[]
for item in range(1,2): 
    inv_info+=getpagecontent(item,COO)

list=applydata_Update_Insert(inv_info)

for item in list:
    print(item)



# for info in inv_info:
#     if len(info)>1:
#        print (info[1])
#        print (info[2])
#        for item in info:
#            print(item)
 
 

 

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