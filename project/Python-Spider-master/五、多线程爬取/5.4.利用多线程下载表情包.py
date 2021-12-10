
import requests
from lxml import etree
from urllib import request
import os
import re
import threading
from queue import Queue

class Producer(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
        'Referer': 'https://movie.douban.com/'
    }

    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Producer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self,url):
        response = requests.get(url,headers=self.headers)
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
            self.img_queue.put((img_url,filename))


class Consumer(threading.Thread):
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Consumer, self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.img_queue.empty() and self.page_queue.empty():
                break
            img_url,filename = self.img_queue.get()
            request.urlretrieve(img_url, 'C:/Users/Administrator/Desktop/images/' + filename)
            print("已下载完一张图片")


def main():
    page_queue = Queue(1000)
    img_queue = Queue(10000)

    for x in range(1,1000):
        url = 'http://www.doutula.com/photo/list/?page=%d'%x
        page_queue.put(url)

    for x in range(10):
        t = Producer(page_queue,img_queue)
        t.start()

    for x in range(10):
        t = Consumer(page_queue,img_queue)
        t.start()

if __name__ == '__main__':
    main()
