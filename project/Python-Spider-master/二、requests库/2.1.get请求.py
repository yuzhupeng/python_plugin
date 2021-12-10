
import requests

params = {
    'wd':'python'
}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
}

response = requests.get("https://www.baidu.com/s",params=params,headers=headers)
#text返回的是unicode的字符串，可能会出现乱码情况
# print(response.text)

#content返回的是字节，需要解码
with open('baidu.html','w',encoding='utf-8') as f:
    f.write(response.content.decode('utf-8'))


# print(response.url)             #https://www.baidu.com/
# print(response.status_code)     #200
# print(response.encoding)        #ISO-8859-1
