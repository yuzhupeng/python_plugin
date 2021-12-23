# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 09:32:22 2021

@author: yunxingluoyun
"""
import requests
import config
import sc.log4
log = sc.log4.get_logger()

def BaiduQuery(address, currentkey):
    """
    address convert lat and lng
    :param address: address
    :param currentkey: AK
    :return: places_ll
    """
    url = 'http://api.map.baidu.com/geocoding/v3/?'
    params = {
        "address": address,
        "city": '东莞市',
        "output": 'json',
        "ak": currentkey,
        "coordtype": "bd09ll",
    }
    response = requests.get(url, params=params)
    answer = response.json()
    # places_ll = []
    if answer['status'] == 0:
        tmpList = answer['result']
        coordString = tmpList['location']
        coordList = [coordString['lng'], coordString['lat']]
        # places_ll.append([address, float(coordList[0]), float(coordList[1])])
        return [address, float(coordList[0]), float(coordList[1])]
    else:
        return -1


    
def reverse_geocoding(lng, lat, currentkey):
    """
    lat and lng convert address
    :param lng: longitude
    :param lat: latitude
    :param currentkey: AK
    :return: places_ll
    """
    url = 'http://api.map.baidu.com/reverse_geocoding/v3/?'
    params = {
        "location": str(lng)+','+str(lat),
        "output": 'json',
        "ak": currentkey,
        "coordtype": "bd09ll",
    }
    response = requests.get(url, params=params)
    answer = response.json()
    if answer['status'] == 0:
        tmpList = answer['result']
        address = tmpList['formatted_address']
        print([lng, lat, address])
        # places_ll.append([address, lng, lat])
    else:
        return -1



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
            coordString = tmpList['location']
            # places_ll.append([address, float(coordList[0]), float(coordList[1])])
            return  coordString
        else:
            return []
    except BaseException as e:
        log.error(f"查询地点信息出错！：Unexpected Error: {e}")

# 测试
address = '广东省东莞市石龙镇西湖社区环湖西路'
currentkey ='5FOb4Fa180itR3lIYyhC2MU7FQEsdBbq'


aaa=get_place_accuracy_direction(address)

# 地理编码
address_LL = BaiduQuery(address, currentkey)

 


print(address_LL)
# 逆地理编码
reverse_geocoding(address_LL[1],address_LL[2], currentkey)





print('1234')


