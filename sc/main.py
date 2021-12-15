#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2021年12月08日15:38:19
# @Author  : kyle (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import requests
import time
import random
import socket
import http.client
import re
from bs4 import BeautifulSoup
import log4 

log = log4.get_logger()
 
# log.debug('I am a debug message')
# log.info('I am a info message')
# log.warning('I am a warning message')
# log.error('I am a error message')
# log.critical('I am a critical message')
    
APPLYLISTURL='http://10.9.140.98/workflow_skc/apps/index.cfm?fuseaction=inquiryall.Apply'
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
            rep = requests.POST(url,headers = _header,data=datas,timeout = timeout,cookies=cookie) #请求url地址，获得返回 response 信息
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

#循环页面获取前七日数据加入到List中
def ApplyNoCalc(cookie):
    results = []
    for item in range(2,10):
         try:
            ApplyListPageDATA="CategoryID=3&BusinessModelAdminID=106&ApplyStatus=-100&ApplyerSection=-100&SApplyDate=&EApplyDate=&SCompleteDate=&ECompleteDate=&SDocApplyDate=&EDocApplyDate=&SDocCompleteDate=&EDocCompleteDate=&PageCount=100&PageNo={_PageNo}&SortKey=ApplyDate&Order=DESC&KeepSortKey=ApplyDate&AdminCD=&SAdminNumber=&EAdminNumber=&AdminCDNumber=&Subject1=&Subject2=&Subject3=&Subject4=&Subject5=&FreeWord=&Lst_ConditionParam=CategoryID%2CBusinessModelAdminID%2CApplyStatus%2CApplyerSection%2CSApplyDate%2CEApplyDate%2CSCompleteDate%2CECompleteDate%2CSDocApplyDate%2CEDocApplyDate%2CSDocCompleteDate%2CEDocCompleteDate%2CPageCount%2CPageNo%2CSortKey%2COrder%2CKeepSortKey%2CAdminCD%2CSAdminNumber%2CEAdminNumber%2CAdminCDNumber%2CSubject1%2CSubject2%2CSubject3%2CSubject4%2CSubject5%2CFreeWord".format(_PageNo=item)
            pagedata= getContent(APPLYLISTURL,datas=ApplyListPageDATA,header=HEADERS,cookie=cookie)          
            soup = BeautifulSoup(pagedata.text, 'lxml')
            table = soup.table;
            tr_arr = table.find_all("tr");
            for tr in tr_arr:
                #//查询所有td
                tds = tr.find_all('td');
                print(tds);
         except Exception as e:
               log.error("循环页面获取前七日数据加入到List中出现异常：Unexpected Error: {}".format(e))
                
        
        
#循环LIST 数据  根据查询的管理序号单进行对比
def getCommentDetail(cookies,itemId=None,currentPage=None):
    APPLYDATA = 'DispType=1&PageCount=100&AdminCD=&SAdminNumber=&EAdminNumber=&AdminCDNumber=&CategoryID=3&BusinessModelAdminID=106&FreeWord=&ApplyerSection=-100&ApplyStatus=-100&Subject1=&Subject2=&Subject3=&Subject4=&Subject5=&SApplyDate=&EApplyDate=&SDocApplyDate=&EDocApplyDate=&SCompleteDate=&ECompleteDate=&SDocCompleteDate=&EDocCompleteDate=&SubBtn=%E8%A1%A8%E7%A4%BA'
    APPLYHEADERS = {
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
    try:
     #serachList=getContent(APPLYLISTURL,datas=APPLYDATA,header=APPLYHEADERS,cookie=cookies)#以100每页全件检索查询
     serachList=requests.post(url=APPLYLISTURL,datas=APPLYDATA,header=APPLYHEADERS,cookie=cookies)#以100每页全件检索查询
     soup = BeautifulSoup(serachList.text, 'lxml')
     table = soup.table;
     tr_arr = table.find_all("tr");
     for tr in tr_arr:
                #//查询所有td
                tds = tr.find_all('td');
                print(tds);
    except Exception as e:
        log.error("循环LIST 数据  根据查询的管理序号单进行对比出错，错误信息：{}".format(e))



#根据管理序号查询是否存在，以及查询状态
def getCasApplyformByNo(applyno):
    print(applyno)

#处理数据更新
def UpdateCasApplyFrom(applyno):
    print('Update CAS单')

#处理数据持久化








if __name__ == '__main__':
    cookie=login()
    getCommentDetail(cookie)
    ApplyNoCalc(cookie)
    print("执行入口的代码")
    print("执行入口的代码")