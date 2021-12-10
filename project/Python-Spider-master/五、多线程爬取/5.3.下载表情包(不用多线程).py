
import requests
from lxml import etree
from urllib import request
import os
import re



def parse_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
        'Referer': 'https://movie.douban.com/'
    }
    response = requests.get(url,headers=headers)
    text = response.text
    html = etree.HTML(text)
    imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
    for img in imgs:
        # print(etree.tostring(img))
        #图片地址
        img_url = img.get('data-original')
        #图片名字
        alt = img.get('alt')
        #替换掉名字里面的特殊字符
        alt = re.sub(r'[\?？\.，。！!\*]','',alt)
        #获取图片的后缀名（.gif .jpg）
        suffix = os.path.splitext(img_url)[1]
        #保存的时候完整的图片名字
        filename = alt + suffix
        request.urlretrieve(img_url,'C:/Users/Administrator/Desktop/images/'+filename)

def main():
    for x in range(1,10):
        url = 'http://www.doutula.com/photo/list/?page=%d'%x
        parse_page(url)

if __name__ == '__main__':
    main()