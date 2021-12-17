 
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
from db2 import DB
import pyslserver
import time
from requests.adapters import HTTPAdapter
requests = requests.Session()
requests.mount('http://', HTTPAdapter(max_retries=3))
requests.mount('https://', HTTPAdapter(max_retries=3))


log = sc.log4.get_logger()


 

def getContent(url,header=None,datas = None,cookie=None):
    i = 0
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

#获取列表数据
def getpagecontent(pageno,cookie):
    url='http://10.9.140.98/workflow_skc/apps/index.cfm?fuseaction=inquiryall.Apply'
    payload = 'DispType=1&PageCount=15&AdminCD=&SAdminNumber=&EAdminNumber=&AdminCDNumber=&CategoryID=11&BusinessModelAdminID=3495&FreeWord=&ApplyerSection=-100&ApplyStatus=-100&Subject1=&Subject2=&Subject3=&Subject4=&Subject5=&SApplyDate=&EApplyDate=&SDocApplyDate=&EDocApplyDate=&SCompleteDate=&ECompleteDate=&SDocCompleteDate=&EDocCompleteDate=&SubBtn=%E8%A1%A8%E7%A4%BA'.format(_PageNo=pageno)
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
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
    except BaseException as  e:
         print(e)
         log.error(f"requests加载用车申请列表信息出错！：Unexpected Error: {e}")
         
    try:   
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
                    # p2 = re.compile(r'[(](.*)[)]', re.S)  #贪婪匹配
                    applyid=re.findall(p1, astr[0].attrs['href'])
                    applyidno = applyid[0].replace('[','').replace(']','')
                    temp.append(applyidno)
                    
            temp.append(tds[5].text.strip())
            inv_info.append(temp)
    
        return inv_info
    except BaseException as e:
 
         log.error(f"解析用车申请列表信息出错！：Unexpected Error: {e}")
         return []
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
            sqlhelper=pyslserver.HandCost('.','sa','1','Skc_Business')
             
            detial=get_apply_data(1,info[1],COO,info[0],info[2])
            sqlhelper.dictToTO(detial)
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
def get_apply_data(pageno,applyids,cookie,applyno,bwfstatus):
     url='http://10.9.140.98/workflow_skc/apps/index.cfm?fuseaction=inquiryall.ApplyDisp&ApplyID={applyid}'.format(applyid=applyids)
     payload = 'CategoryID=11&BusinessModelAdminID=3495&ApplyStatus=-100&ApplyerSection=-100&SApplyDate=&EApplyDate=&SCompleteDate=&ECompleteDate=&SDocApplyDate=&EDocApplyDate=&SDocCompleteDate=&EDocCompleteDate=&PageCount=15&PageNo=={_PageNo}&SortKey=ApplyDate&Order=DESC&KeepSortKey=ApplyDate&AdminCD=&SAdminNumber=&EAdminNumber=&AdminCDNumber=&Subject1=&Subject2=&Subject3=&Subject4=&Subject5=&FreeWord=&Lst_ConditionParam=CategoryID%2CBusinessModelAdminID%2CApplyStatus%2CApplyerSection%2CSApplyDate%2CEApplyDate%2CSCompleteDate%2CECompleteDate%2CSDocApplyDate%2CEDocApplyDate%2CSDocCompleteDate%2CEDocCompleteDate%2CPageCount%2CPageNo%2CSortKey%2COrder%2CKeepSortKey%2CAdminCD%2CSAdminNumber%2CEAdminNumber%2CAdminCDNumber%2CSubject1%2CSubject2%2CSubject3%2CSubject4%2CSubject5%2CFreeWord'.format(_PageNo=pageno)
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
     try:
        response = requests.request("POST", url, headers=headers, data=payload)
     except BaseException as e:
         log.error(f"request获取明细信息出错，错误单号：{applyno}：Unexpected Error: {e}")
           
     try:
            html_text = response.content.decode("utf-8")
     except UnicodeDecodeError as e:
            print("解码api响应内容失败")

            log.error(f"request获取明细信息出错，错误单号：{applyno}：Unexpected Error: {e}")
            return
     xphtml = etree.HTML(html_text)
      
     try:
            inputs = xphtml.xpath("//table")
            table2=inputs[5]
            applytpye=table2.xpath("./tr[1]/td/table/tr/td[2]/span/textarea")[0].text#申请用车类型 
            AcutalUser=table2.xpath("./tr[2]/td/table/tr/td[4]/span/input")[0].get('value', default=None)#实际使用者
            Peoples=table2.xpath("./tr[2]/td/table/tr/td[2]/span/input")[0].get('value', default=None)#实际人数
            InSideLine=table2.xpath("./tr[2]/td/table/tr/td[6]/span/input")[0].get('value', default=None)#内线
            reason=table2.xpath("./tr[1]/td/table/tr/td[4]/span/input")[0].get('value', default=None)#变更、取消理由
            usereason=table2.xpath("./tr[6]/td/table/tr/td[2]/span/input")[0].get('value', default=None)#用车理由
            DetailedAddres=table2.xpath("./tr[7]/td/table/tr/td[2]/span/input")[0].get('value', default=None)#行程详细地址
    
            phone1=table2.xpath("./tr[8]/td/table/tr/td[2]/span/input")[0].get('value', default=None)#联系人手机
            passenger1=table2.xpath("./tr[8]/td/table/tr/td[4]/span/input")[0].get('value', default=None)#联系人1 
            
            phone2=table2.xpath("./tr[9]/td/table/tr/td[2]/span/input")[0].get('value', default=None)#联系人手机
            passenger2=table2.xpath("./tr[9]/td/table/tr/td[4]/span/input")[0].get('value', default=None)#联系人2 
            
            phone3=table2.xpath("./tr[10]/td/table/tr/td[2]/span/input")[0].get('value', default=None)#联系人手机
            passenger3=table2.xpath("./tr[10]/td/table/tr/td[4]/span/input")[0].get('value', default=None)#联系人3 
            
            phone4=table2.xpath("./tr[11]/td/table/tr/td[2]/span/input")[0].get('value', default=None)#联系人手机
            passenger4=table2.xpath("./tr[11]/td/table/tr/td[4]/span/input")[0].get('value', default=None)#联系人4 
            
            phone5=table2.xpath("./tr[12]/td/table/tr/td[2]/span/input")[0].get('value', default=None)#联系人手机
            passenger5=table2.xpath("./tr[12]/td/table/tr/td[4]/span/input")[0].get('value', default=None)#联系人5 
            
  
            ShareCore=table2.xpath("./tr[14]/td/table/tr/td[2]/span/input")[0].get('value', default=None)#经费代码
            CostDepartment=table2.xpath("./tr[13]/td/table/tr/td[4]/span/input")[0].get('value', default=None)#部门
            applyperson=table2.xpath("./tr[21]/td/table/tr[5]/td[2]/span")[0].text#申请人
            applydate=table2.xpath("./tr[21]/td/table/tr[6]/td[2]/span")[0].text#申请日期
            createtime= (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            Company=table2.xpath("./tr[13]/td/table/tr/td[2]/span/textarea")[0].text#公司
            
            #/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[2]/td/table/tbody/tr[8]/td/table/tbody/tr/td[2]/span/input 手机1
            #/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[2]/td/table/tbody/tr[8]/td/table/tbody/tr/td[4]/span/input 乘车人1
            
            
            #/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[2]/td/table/tbody/tr[9]/td/table/tbody/tr/td[2]/span/input
            #/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[2]/td/table/tbody/tr[9]/td/table/tbody/tr/td[4]/span/input
            
            #/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[2]/td/table/tbody/tr[12]/td/table/tbody/tr/td[2]/span/input
            #/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/span/input
            
            
            table3=inputs[9]
            TravelDetial=[]
            trs=table3.xpath("./tr")
            for item in trs:       
                tds=item.xpath("./td")
                if len(tds)>0:
                    vasq=tds[1].xpath("./span/input")[0]
                    usedate= tds[1].xpath("./span/input")[0].get('value', default=None)#用车日期
                    start= tds[2].xpath("./span/input")[0].get('value', default=None)#出发地                     
                    travel1= tds[3].xpath("./span/input")[0].get('value', default=None)#目的地1
                    travel2= tds[4].xpath("./span/input")[0].get('value', default=None)#目的地2
                    travel3= tds[5].xpath("./span/input")[0].get('value', default=None)#目的地3
                    travel4= tds[6].xpath("./span/input")[0].get('value', default=None)#目的地4
                    travel5= tds[7].xpath("./span/input")[0].get('value', default=None)#目的地5
                    travel6= tds[8].xpath("./span/input")[0].get('value', default=None)#目的地6
                    OstartTime= tds[9].xpath("./span/input")[0].get('value', default=None)#出发日期  
                    ReturnTime= tds[10].xpath("./span/input")[0].get('value', default=None)#返回日期  
                    FlightNo= tds[11].xpath("./span/input")[0].get('value', default=None)#航班号    
                    FlightTime= tds[12].xpath("./span/input")[0].get('value', default=None)#起飞到达日期
                    detials={'usedate':usedate,'travel1':travel1,'travel2':travel2,'travel3':travel3,'travel4':travel4,'travel5':travel5,'travel6':travel6,'start':start,'OstartTime':OstartTime,'ReturnTime':ReturnTime,'FlightNo':FlightNo,'FlightTime':FlightTime}
                    TravelDetial.append(detials)
            
            applyform= {'applyno':applyno,'Peoples':Peoples,'bwfstatus':bwfstatus,'AcutalUser':AcutalUser,'InSideLine':InSideLine,'Company':Company,'applytype':applytpye,'reason':reason,'userason':usereason,'DetailedAddres':DetailedAddres,
            'passenger1':passenger1,'passenger2':passenger2,'passenger3':passenger3,'passenger4':passenger4,'passenger5':passenger5,'phone1':phone1,'phone2':phone2,'phone3':phone3,'phone4':phone4,'phone5':phone5,'ShareCore':ShareCore,'CostDepartment':CostDepartment,'applyperson':applyperson,'applydate':applydate
            ,'createtime':createtime,'TravelDetial':TravelDetial}
            detial=[]
            detial.append(applyform)
            #经费负担部门
            return applyform
     except BaseException as e:
         
            log.error(f"解析明细信息出错，错误单号：{applyno}：Unexpected Error: {e}")
            return []
    




COO='CFID=4243124; CFTOKEN=12412058'
log.info('ces')
log.info('hello')
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