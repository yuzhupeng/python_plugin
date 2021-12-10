
from urllib import request,parse

url = "https://www.baidu.com/s?wd=cnblog#2"
result = parse.urlparse(url)
print(result)
#ParseResult(scheme='https', netloc='www.baidu.com', path='/s', params='', query='wd=cnblog', fragment='2')

print('scheme:',result.scheme)   #协议
print('netloc:',result.netloc)   #域名
print('path:',result.path)       #路径
print('query:',result.query)     #查询参数

#结果
#scheme: https
# netloc: www.baidu.com
# path: /s
# query: wd=cnblog


#urlparse和urlsplit都是用来对url的各个组成部分进行分割的，唯一不同的是urlsplit没有"params"这个属性.