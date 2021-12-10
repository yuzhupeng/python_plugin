#urlencode函数

# 简单用法
#from urllib import parse
# data = {'name':'德瑞克','age':100}
# qs = parse.urlencode(data)
# print(qs)    #name=%E5%BE%B7%E7%91%9E%E5%85%8B&age=100

#实际用例
# from urllib import request,parse
# url = "http://www.baidu.com/s"
# params = {"wd":"博客园"}
# qs = parse.urlencode(params)
# url = url + "?" + qs
# res = request.urlopen(url)
# print(res.read())

#parse_qs的用法
from urllib import parse

qs = "name=%E5%BE%B7%E7%91%9E%E5%85%8B&age=100"
print(parse.parse_qs(qs))   #{'name': ['德瑞克'], 'age': ['100']}
