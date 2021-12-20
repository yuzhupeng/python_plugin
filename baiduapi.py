import json
from math import radians, cos, sin, asin, sqrt 
import requests
 
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
def getPositions(ak, dw):
    #url = 'http://api.map.baidu.com/geocoding/v3/?address={Address}&output=json&ak={Ak}'.format(Address=dw, Ak=ak)
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

#根据简称获取详细信息
def getFullAddressbyabbreviation(address):
    print('')



if __name__ == '__main__':
    ak = '5FOb4Fa180itR3lIYyhC2MU7FQEsdBbq'
    ad='社贝村'
    getPositions(ak,ad)
    
    
    
    place1=input("输入起点:")
    place11=getplace_update(ak,place1)
    print(place11)
    place2=input("输入终点:")
    place22=getplace_update(ak,place2)
    print(place22)
    distance = calDistance(ak,place1,place2)
    print("%s"%place11,"和%s之间的距离"%place22,"为%d千米"%distance)