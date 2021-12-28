from urllib import request, parse

# url = 'https://www.qiushibaike.com/text/'

# resp = request.urlopen(url)
# print(resp.read())
# resp = request.urlretrieve(url, 'baidu.gif')

# data = {"name": "张三", "age": 18, "interest": "playgame"}
# encode_data = parse.urlencode(data)
# print(encode_data)

# qs_data = parse.parse_qs(encode_data)
# print(qs_data)

# result = parse.urlparse(url)
# print(result)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
}
#
# req = request.Request(
#     url=url, headers=headers
# )
# resp = request.urlopen(req)
# print(resp.read())

# handler = request.ProxyHandler({"http": "106.55.15.244:8889"})
# opener = request.build_opener(handler)
# req = request.Request('http://httpbin.org/ip')
# resp = opener.open(req)
# print(resp.read())
# handler = request.ProxyHandler({"http":"58.47.159.147:8001"})
#
# opener = request.build_opener(handler)
# req = request.Request("http://httpbin.org/ip", headers=headers)
# resp = opener.open(req)
# print(resp.read())
#
# url = "https://music.163.com/weapi/cloudsearch/get/web?csrf_token="
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
# }
#
# formdata = {
#     "params": "xBbvUcsF0gWSp5lindtB8SJZJGA2IGh3PpOujT3EVRuagrdEhx/+dCUkk7ooMa7vUe6ys+4gwPpYpklC5fSZcNC+LkJEesr1mms/MxwiiQLi41AZvbTi/QgNRYy0IWL1sQApT4rkmNUaWu6oMXUmcfXhVj5q/ixOYp3oKqEh9mqdpt0tA48YeCE60WZfio+QP0ts5YXFQmRzevTE2veBBiQJy4SNU7vU7DO2u5ZVPkTxH1mTKoCYYYtBRswboUFL3vDlEOz66WdA4ILxg1AwKsO3Gxz8+ylI6KekiJYwDco=",
#     "encSecKey": "355403235b4cd9c41293e66ea208b029e9a5feb2bb1cac821c5c6041c3efa7fc3f4962e0961c39e95ef487679b5d3c54e22f42f91d41aaa91dc0068c1e2ee41376ddf1af006ce9bc2253df47b445b4db597828aeb9da5c3d06f96634e31cb9838cc80d7a077f149c5b9b9d14f6c1110c03a00246d2f367656fb28e509c2f684b"
# }
#
# req = request.Request(url, headers=headers, data=parse.urlencode(formdata).encode('utf-8'))
# resp = request.urlopen(req)
# print(resp.read().decode('utf-8'))

# _headers = {}
# i = _headers.get("TankHeatpump", 0)
# print(len(i))
# print(i)
try:
    a = 1/0
except Exception as e:
    print(e)

print("完成")

