#encoding:utf-8

from urllib import request

res = request.urlopen("https://www.cnblogs.com/")

print(res.readlines())


#urlopen的参数
#def urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
#            *, cafile=None, capath=None, cadefault=False, context=None):