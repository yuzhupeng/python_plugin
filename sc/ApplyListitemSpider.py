import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
import model.ApplyListitem


# 创建一个爬虫类
class ApplyListitemSpider:
    def __init__(self):
        self.url = 'http://10.9.140.98/workflow_skc/logon/index.cfm'
  
        

def get_pagedata(self, pageno,res):
     
    soup = BeautifulSoup(res.text, "lxml")
    table = soup.table;
    tr_arr = table.find_all("tr");
    for tr in tr_arr:
        #//查询所有td
        tds = tr.find_all('td');
        print(tds);
        