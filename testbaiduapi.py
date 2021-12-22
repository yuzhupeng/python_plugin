# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 09:32:22 2021

@author: yunxingluoyun
"""
import requests

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
        "location": str(lat)+','+str(lng),
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


# 测试
address = '广东省东莞市京瓷路8号'
currentkey ='5FOb4Fa180itR3lIYyhC2MU7FQEsdBbq'

# 地理编码
address_LL = BaiduQuery(address, currentkey)
print(address_LL)
# 逆地理编码
reverse_geocoding(address_LL[1],address_LL[2], currentkey)


print('1234')


