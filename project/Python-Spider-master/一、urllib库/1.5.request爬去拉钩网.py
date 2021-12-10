#利用Request类爬去拉勾网职位信息

from urllib import request,parse

url = "https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false"

#请求头
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36",
    "Referer":"https://www.lagou.com/jobs/list_python?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput="
}
#post请求需要提交的数据
data = {
    'first':'true',
    'pn':1,
    'kd':'python'
}
#post请求的data数据必须是编码后的字节类型
req = request.Request(url,headers=headers,data=parse.urlencode(data).encode('utf-8'),method='POST')   #建立一个请求对象
res = request.urlopen(req)
#获取的信息是字节类型，需要解码
print(res.read().decode('utf-8'))
