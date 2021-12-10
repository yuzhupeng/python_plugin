# -*- coding: utf-8 -*-
import scrapy
import re
from fang.items import NewHouseItem,ESFHouseItem

class SfwSpiderSpider(scrapy.Spider):
    name = 'sfw_spider'
    allowed_domains = ['fang.com']
    start_urls = ['http://www.fang.com/SoufunFamily.htm']

    def parse(self, response):
        trs = response.xpath("//div[@class='outCont']//tr")
        provice = None
        for tr in trs:
            #排除掉第一个td，两个第二个和第三个td标签
            tds = tr.xpath(".//td[not(@class)]")
            provice_td = tds[0]
            provice_text = provice_td.xpath(".//text()").get()
            #如果第二个td里面是空值，则使用上个td的省份的值
            provice_text = re.sub(r"\s","",provice_text)
            if provice_text:
                provice = provice_text
            #排除海外城市
            if provice == '其它':
                continue

            city_td = tds[1]
            city_links = city_td.xpath(".//a")
            for city_link in city_links:
                city = city_link.xpath(".//text()").get()
                city_url = city_link.xpath(".//@href").get()
                # print("省份：",provice)
                # print("城市：",city)
                # print("城市链接：",city_url)
                #下面通过获取的city_url拼接出新房和二手房的url链接
                #城市url：http://cq.fang.com/
                #新房url:http://newhouse.cq.fang.com/house/s/
                #二手房：http://esf.cq.fang.com/
                url_module = city_url.split("//")
                scheme = url_module[0]     #http:
                domain = url_module[1]     #cq.fang.com/
                if 'bj' in domain:
                    newhouse_url = ' http://newhouse.fang.com/house/s/'
                    esf_url = ' http://esf.fang.com/'
                else:
                    #新房url
                    newhouse_url = scheme + '//' + "newhouse." + domain + "house/s/"
                    #二手房url
                    esf_url = scheme + '//' + "esf." + domain + "house/s/"
                # print("新房链接：",newhouse_url)
                # print("二手房链接：",esf_url)

                #meta里面可以携带一些参数信息放到Request里面，在callback函数里面通过response获取
                yield scrapy.Request(url=newhouse_url,
                                     callback=self.parse_newhouse,
                                     meta = {'info':(provice,city)}
                                     )

                yield scrapy.Request(url=esf_url,
                                     callback=self.parse_esf,
                                     meta={'info': (provice, city)})


    def parse_newhouse(self,response):
        #新房
        provice,city = response.meta.get('info')
        lis = response.xpath("//div[contains(@class,'nl_con')]/ul/li")
        for li in lis:
            name = li.xpath(".//div[contains(@class,'house_value')]//div[@class='nlcd_name']/a/text()").get()
            if name:
                name = re.sub(r"\s","",name)
                #居室
                house_type_list = li.xpath(".//div[contains(@class,'house_type')]/a/text()").getall()
                house_type_list = list(map(lambda x:re.sub(r"\s","",x),house_type_list))
                rooms = list(filter(lambda x:x.endswith("居"),house_type_list))
                #面积
                area = "".join(li.xpath(".//div[contains(@class,'house_type')]/text()").getall())
                area = re.sub(r"\s|－|/","",area)
                #地址
                address = li.xpath(".//div[@class='address']/a/@title").get()
                address = re.sub(r"[请选择]","",address)
                sale = li.xpath(".//div[contains(@class,'fangyuan')]/span/text()").get()
                price = "".join(li.xpath(".//div[@class='nhouse_price']//text()").getall())
                price = re.sub(r"\s|广告","",price)
                #详情页url
                origin_url = li.xpath(".//div[@class='nlcd_name']/a/@href").get()

                item = NewHouseItem(
                    name=name,
                    rooms=rooms,
                    area=area,
                    address=address,
                    sale=sale,
                    price=price,
                    origin_url=origin_url,
                    provice=provice,
                    city=city
                )
                yield item

        #下一页
        next_url = response.xpath("//div[@class='page']//a[@class='next']/@href").get()
        if next_url:
            yield scrapy.Request(url=response.urljoin(next_url),
                                 callback=self.parse_newhouse,
                                 meta={'info': (provice, city)}
                                 )


    def parse_esf(self,response):
        #二手房
        provice, city = response.meta.get('info')
        dls = response.xpath("//div[@class='shop_list shop_list_4']/dl")
        for dl in dls:
            item = ESFHouseItem(provice=provice,city=city)
            name = dl.xpath(".//span[@class='tit_shop']/text()").get()
            if name:
                infos = dl.xpath(".//p[@class='tel_shop']/text()").getall()
                infos = list(map(lambda x:re.sub(r"\s","",x),infos))
                for info in infos:
                    if "厅" in info:
                        item["rooms"] = info
                    elif '层' in info:
                        item["floor"] = info
                    elif '向' in info:
                        item['toward'] = info
                    elif '㎡' in info:
                        item['area'] = info
                    elif '年建' in info:
                        item['year'] = re.sub("年建","",info)
                item['address'] = dl.xpath(".//p[@class='add_shop']/span/text()").get()
                #总价
                item['price'] = "".join(dl.xpath(".//span[@class='red']//text()").getall())
                #单价
                item['unit'] = dl.xpath(".//dd[@class='price_right']/span[2]/text()").get()
                item['name'] = name
                detail = dl.xpath(".//h4[@class='clearfix']/a/@href").get()
                item['origin_url'] = response.urljoin(detail)
                yield item
        #下一页
        next_url = response.xpath("//div[@class='page_al']/p/a/@href").get()
        if next_url:
            yield scrapy.Request(url=response.urljoin(next_url),
                                 callback=self.parse_esf,
                                 meta={'info': (provice, city)}
                                 )

