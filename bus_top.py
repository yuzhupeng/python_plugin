import requests
import json
from bs4 import BeautifulSoup
import pandas as pd

class bus_stop:
 ## 定义一个类，用来获取每趟公交的站点名称和经纬度
    def __init__(self):
     self.url = 'https://guiyang.8684.cn/line1{}'
     self.starnum = []
     for start_num in range(1, 17):
      self.starnum.append(start_num)
      self.payload = {}
      self.headers = {
    'Cookie': 'JSESSIONID=48304F9E8D55A9F2F8ACC14B7EC5A02D'}
    ## 调用高德api获取公交线路的经纬度
    ### 这个key大家可以自己去申请
    def get_location(self, line):
      url_api = 'https://restapi.amap.com/v3/bus/linename?s=rsv3&extensions=all&key=559bdffe35eec8c8f4dae959451d705c&output=json&city=东莞&offset=2&keywords={}&platform=JS'.format(
     line)
      res = requests.get(url_api).text
    # print(res) 可以用于检验传回的信息里面是否有自己需要的数据
      rt = json.loads(res)
      dicts = rt['buslines'][0]
    # 返回df对象
      df = pd.DataFrame.from_dict([dicts])
      return df
   
   
   
 ## 获取每趟公交的站点名称
    def get_line(self):
     for start in self.starnum:
        start = str(start)
    # 构造url
     url = self.url.format(start)
     res = requests.request(
    "GET", url, headers=self.headers, data=self.payload)
     soup = BeautifulSoup(res.text, "lxml")
     div = soup.find('div', class_='list clearfix')
     lists = div.find_all('a')
     for item in lists:
       line = item.text  # 获取a标签下的公交线路 
       lines.append(line)
       return lines
if __name__ == '__main__':
    bus_stop = bus_stop()
    stop_df = pd.DataFrame([])
    lines = []
    bus_stop.get_line()
    # 输出路线
    print('一共有{}条公交路线'.format(len(lines)))
    print(lines)
    # 异常处理
    error_lines = []
    for line in lines:
     try:
         df = bus_stop.get_location(line)
         stop_df = pd.concat([stop_df, df], axis=0)
     except:
        error_lines.append(line)

    # 输出异常的路线 
    print('异常路线有{}条公交路线'.format(len(error_lines))) 
    print(error_lines)

    # 输出文件大小 
    print(stop_df.shape)
    stop_df.to_csv('bus_stop.csv', encoding='gbk', index=False)