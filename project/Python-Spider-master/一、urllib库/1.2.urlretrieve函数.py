#coding:utf-8

from urllib import request

res = request.urlretrieve("https://www.cnblogs.com/",'cnblog.html')


#urlretrieve参数
#def urlretrieve(url, filename=None, reporthook=None, data=None):