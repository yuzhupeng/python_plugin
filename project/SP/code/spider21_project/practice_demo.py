
import re
import requests
from lxml import etree

url = "http://www.gushiwen.org/default_1.aspx"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
}

response = requests.get(url, headers=headers)

html = etree.HTML(response.content.decode())

ul_list = html.xpath('/html/body/div[2]/div[1]')[0]
for div in ul_list:
    sons = div.xpath('.//')[0]



