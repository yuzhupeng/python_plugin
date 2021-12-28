import requests
from lxml import etree


# 请求头
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    'Referer': 'https://www.dydytt.net/index2.htm'
}

start_url = "https://www.dydytt.net/html/gndy/dyzz/index.html"


response = requests.get(start_url,headers=headers)
# with open('dytt.html', 'wb') as file:
#     file.write(response.content)

html = etree.HTML(response.text)
ul_list = html.xpath('//*[@id="header"]/div/div[3]/div[3]/div[2]/div[2]/div[2]/ul')[0]
for ul in ul_list:
    # title = ul.xpath('./tbody/tr[2]/td[2]/b/a/text()')[0]
    print(ul)


