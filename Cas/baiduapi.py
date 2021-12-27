import json
from math import radians, cos, sin, asin, sqrt
from typing import List 
import requests
import sqlpymssql
import config
import log4
log = log4.get_logger()
import numpy

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


def getPositionMap(address):
    """
    address convert lat and lng
    :param address: address
    :param currentkey: AK
    :return: places_ll
    """
    test = config.ReadConfig()
    ak=test.get_other('ak')
    url = 'http://api.map.baidu.com/geocoding/v3/?'
    params = {
        "address": address,
        "city": '东莞市',
        "output": 'json',
        "ak": ak,
    }
    response = requests.get(url, params=params)
    answer = response.json()
    # places_ll = []
    if answer['status'] == 0:
        tmpList = answer['result']
        coordString = tmpList['location']
        coordList = [coordString['lng'], coordString['lat']]
        # places_ll.append([address, float(coordList[0]), float(coordList[1])])
        return [address, round(float(coordList[0]),6), round(float(coordList[1]),6)]
    else:
        return []


#根据经纬度获取详细地址信息
#lat 维度  lng 经度
def getAddressbyPostions(lat,lng):
    try:
        test = config.ReadConfig()
        ak=test.get_other('ak')
        urls=f'https://api.map.baidu.com/reverse_geocoding/v3/?ak={ak}&output=json&coordtype=bd09ll&location={lat},{lng}'
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
            return get_place_accuracy_direction(detial)
        else:
             
            return get_place_accuracy_direction(address)
    except BaseException as e:
           log.error(f"调用百度api获取地点信息出错！：Unexpected Error: {e}")

#查询路线规划信息
def get_driving_direction(start,end):
    try:
        test = config.ReadConfig()
        ak=test.get_other('ak')
        startresult=getplace_byabbreviation(start)#查询常用地点并转化为经度纬度
        endresult=getplace_byabbreviation(end)#查询常用地点并转化为经度纬度
        
        if startresult==None or endresult ==None or len(startresult)==0 or len(endresult)==0:
            log.error(f"调用百度api获取地点信息出错！：出发点和目的地: {start}-------{end}")
            return []
        
        
        startlat=startresult['location']['lat']
        startlng=startresult['location']['lng']
        startuid=startresult['uid']
        startplace=startresult['address']+'('+startresult['province']+'--'+startresult['city']+')'
        
        
        endlat= endresult['location']['lat']
        endlng=endresult['location']['lng']
        enduid=endresult['uid']
        endplace=endresult['address']+'('+endresult['province']+'--'+endresult['city']+')'
        
        url = 'https://api.map.baidu.com/direction/v2/driving?'
        params = {
            "origin": str(startlat)+','+str(startlng),
            "destination":str(endlat)+','+str(endlng) ,
            "origin_uid":startuid,
            "destination_uid":enduid,
            "output": 'json',
            "ak": ak,
        }
        res = requests.get(url, params=params)
        if res:
            json_data = json.loads(res.text)
            tmpList = json_data['result']
            coordString = tmpList['routes'][0]
            
            distance=coordString['distance']/1000
            duration=round((coordString['duration']/60),2)
            
            tolls=sum(item['toll'] for item in coordString['steps'])
        
            return [distance,duration,tolls,startplace,endplace]
    except BaseException as e:
           log.error(f"调用百度api获取地点信息出错！：Unexpected Error: {e}")
           log.error(f"调用百度api获取地点信息出错！：出发点和目的地: {start}-------{end}")
           return []

 
 
 
 
def get_place_accuracy_direction(address):
    try:
        print(0)
     
        test = config.ReadConfig()
        ak=test.get_other('ak')
        url = 'https://api.map.baidu.com/place/v2/search?'
        params = {
            "query": address,
            "region": '东莞市',
            "output": 'json',
            "ak": ak,
        }
        response = requests.get(url, params=params)
        answer = response.json()
        # places_ll = []
        if answer['status'] == 0:
            tmpList = answer['results'][0]
            # coordString = tmpList['location']
            # places_ll.append([address, float(coordList[0]), float(coordList[1])])
            return  tmpList
        else:
            return []
    except BaseException as e:
        log.error(f"查询地点信息出错！：Unexpected Error: {e}")


if __name__ == '__main__':
    # ak = '5FOb4Fa180itR3lIYyhC2MU7FQEsdBbq'
    # ad='社贝村'
    # getPositions(ak,ad)
    result=get_driving_direction('SKC','濠兴海鲜酒楼')
 
    
    
    
    
    
   # result=getplace_byabbreviation('SKC')
    # latlng=getPositions('社贝村')
    # addressdetial=getAddressbyPostions(latlng[0],latlng[1])
 
    
    
    
    
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