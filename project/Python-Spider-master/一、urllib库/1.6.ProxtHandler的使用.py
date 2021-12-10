
#代理的使用
from urllib import request

url = "https://www.baidu.com/s?wd=cnblog"

#1.使用ProxyHandler传入代理构建一个handler
# handler = request.ProxyHandler({'http':'115.210.31.236.55:9000'})
handler = request.ProxyHandler({'http':'115.210.31.236.55:9000'})
#2.使用创建的handler构建一个opener
opener = request.build_opener(handler)
#3.使用opener去发送一个请求
res = opener.open(url)
print(res.read())