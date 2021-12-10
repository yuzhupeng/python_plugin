
import requests

proxy = {'http':'115.210.31.236.55:9000'}

response = requests.get("https://www.baidu.com/",proxies=proxy)

print(response.content.decode('utf-8'))
