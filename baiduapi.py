import json
from math import radians, cos, sin, asin, sqrt
from typing import List 
import requests
import sqlpymssql
import config
import sc.log4
log = sc.log4.get_logger()


#根据地址返回经纬度 
def getPosition(ak, dw):
    url = 'http://api.map.baidu.com/geocoding/v3/?address={Address}&output=json&ak={Ak}'.format(Address=dw, Ak=ak)
    res = requests.get(url)
    json_data = json.loads(res.text)
    if json_data['status'] == 0:
        lat = json_data['result']['location']['lat']  # 纬度
        lng = json_data['result']['location']['lng']  # 经度
    else:
        print("Error output!")
        print(json_data)
        return json_data['status']
    return lat,lng

#暂时未使用
def calDistance(ak,place1,place2):
    '''
    输入两个地点名，输出直线距离(千米)
    place1：地点1
    place2：地点2
    '''
    lat1,lng1 = getPosition(ak,place1)#经纬度1
    lat2,lng2 = getPosition(ak,place2)#经纬度2
    lng1, lat1, lng2, lat2 = map(radians, [float(lng1), float(lat1), float(lng2), float(lat2)]) # 经纬度转换成弧度
    dlon=lng2-lng1
    dlat=lat2-lat1
    a=sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    distances =2*asin(sqrt(a))*6371*1000 # 地球平均半径，6371km
    distance= round(distances/1000,3)
    return distance
#返回详细地址
def getplace_update(ak, dw):
    add_url = 'http://api.map.baidu.com/geocoding/v3/?address={Address}&output=json&ak={Ak}'.format(Address=dw, Ak=ak)
    (lat, lng) = getPosition(ak,add_url)
    url = 'http://api.map.baidu.com/reverse_geocoding/v3/?ak=' + ak + '&output=json&coordtype=wgs84ll&location='+str(lat)+','+str(lng)
    result = requests.get(url)
    text = json.loads(result.text)
    address = text.get('result').get('addressComponent')
    city = address.get('city')
    province = address.get('province')
    district = address.get('district')
    if city == province:
        place = province+district
    else:
        place = province + city + district
    return place


#根据地址返回经纬度 
def getPositions(dw):
    test = config.ReadConfig()
    ak=test.get_other('ak')
   
    urls='https://api.map.baidu.com/geocoding/v3/?address={Address}&output=json&ak={Ak}'.format(Address=dw, Ak=ak)
    res = requests.get(urls)
    json_data = json.loads(res.text)
    if json_data['status'] == 0:
        lat = json_data['result']['location']['lat']  # 纬度
        lng = json_data['result']['location']['lng']  # 经度
    else:
        print("Error output!")
        print(json_data)
        return json_data['status']
    return lat,lng

#根据经纬度获取详细地址信息
#lat 维度  lng 经度
def getAddressbyPostions(lat,lng):
    try:
        test = config.ReadConfig()
        ak=test.get_other('ak')
        urls=f'https://api.map.baidu.com/reverse_geocoding/v3/?ak={ak}&output=json&coordtype=wgs84ll&location={lat},{lng} '
        res = requests.get(urls)
        json_data = json.loads(res.text)
        return json_data
    except BaseException as e:
        log.error(f"根据经度纬度查询地点信息出错！：Unexpected Error: {e}")

#根据简称获取详细信息
def getFullAddressbyabbreviation(address):
    try:
         sqlhelper=sqlpymssql.SQLHelp('.','sa','1','Skc_Business')
         addresssql=f'select top 1* from CasDestination where  VagueLocation like \'%{address}%\''
         return sqlhelper.get_data(addresssql)
    except BaseException as e:
           log.error(f"查询常用地点信息出错！：Unexpected Error: {e}")
    

#获取 地点详细信息
def getplace_byabbreviation(address):
     
    try:
        actualaddress= getFullAddressbyabbreviation(address)
        if len(actualaddress)==1:
            detial=actualaddress[0][2]
            return getPositions(detial)
        else:
            return getPositions(address)
    except BaseException as e:
           log.error(f"调用百度api获取地点信息出错！：Unexpected Error: {e}")

#查询路线规划信息出错
def get_driving_direction(start,end):
    try:
        test = config.ReadConfig()
        ak=test.get_other('ak')
        startresult=getplace_byabbreviation(start)
        endresult=getplace_byabbreviation(end)
        starts=startresult[0]
        starte=startresult[1]
         
        ends=endresult[0]
        ende=endresult[1]
        
        urls=f'https://api.map.baidu.com/direction/v2/driving?origin={starts},{starte}&destination={ends},{ende}&ak={ak}'
        res = requests.get(urls)
        json_data = json.loads(res.text)
        return json_data
    except BaseException as e:
           log.error(f"调用百度api获取地点信息出错！：Unexpected Error: {e}")
     


if __name__ == '__main__':
    # ak = '5FOb4Fa180itR3lIYyhC2MU7FQEsdBbq'
    # ad='社贝村'
    # getPositions(ak,ad)
    
   # result=getplace_byabbreviation('SKC')
    result=get_driving_direction('社贝村','白云机场')
    SQ= getFullAddressbyabbreviation('SKC')
    if len(SQ)==1:
       aw=SQ[0][2]
 
    
    place1=input("输入起点:")
    place11=getplace_update(place1)
    print(place11)
    place2=input("输入终点:")
    place22=getplace_update(place2)
    print(place22)
    distance = calDistance(place1,place2)
    print("%s"%place11,"和%s之间的距离"%place22,"为%d千米"%distance)