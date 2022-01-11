import requests
from lxml import etree
import os,sys


def parse_list_page(source):
        html = etree.HTML(source)
        try:
            ul_list = html.xpath('//*[@class="job-list"]/ul')[0]
        except IndexError:
            try:
                status = int(html.xpath('//*[@class="text"]/h1/text()')[0])
                if status == 403:
                    print('ip被封')
                    return 0
            except Exception as e:
                try:
                    button = str(html.xpath('//*[@class="btn"]/text()')[0])
                    if button == '点击进行验证':
                        print('手动验证ip重新访问')
                    else:
                        print('ip被封')
                    return 0
                except Exception as e:
                    print('请求失败，换个ip')
                    return 0
        result_list = []
        for li in ul_list:
            params = {}
            hres=li.xpath('.//*[@class="job-name"]/a')[0].get("href")
            params["job_detial_url"] = 'https://www.zhipin.com'+hres
            params["job_name"] = li.xpath('.//*[@class="job-name"]/a/text()')[0]
            params["job-area"] = li.xpath('.//*[@class="job-area"]/text()')[0]
            params["job_money"] = li.xpath('.//*[@class="job-limit clearfix"]/span/text()')[0]
            params["job_work"] = li.xpath('.//*[@class="job-limit clearfix"]/p/text()')[0]
            params["job_education"] = li.xpath('.//*[@class="job-limit clearfix"]/p/text()')[1]
            params["company_name"] = li.xpath('.//*[@class="company-text"]/h3/a/text()')[0]
            result_list.append(params)
        print('=' * 100)
        print(result_list)
        # return 1











root = 'E:\\python\\100day\\project\\SP\\code\\\lagou_spider'
list = os.listdir('E:\\python\\100day\\project\\SP\\code\\\lagou_spider')#列出目录下的所有文件和目录
os.chdir(root)
headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9,und;q=0.8,en;q=0.7',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': 'lastCity=101281600; __zp_seo_uuid__=881a22aa-06dd-4cde-a373-357f5849fd47; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1640673417,1640673423; acw_tc=0bdf718c16418908183251213e4561695ee973938a427e4a6bfc7ebfbea422; wd_guid=4c29780c-91c5-41ed-aa78-fac31c5c3d06; historyState=state; __fid=a9cb9067b846c0af08a0fb77a05015ff; __l=r=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DHva9PkVwYZv8KSEWftSqTO3FFLR6FG2N2GIf_1iT5FwtIaMC5cLixPpQxlJXwPsA%26wd%3D%26eqid%3Dffc1b5d600097e240000000661cab083&l=%2Fwww.zhipin.com%2Fjob_detail%2F%3Fquery%3Dpython%26city%3D101281600%26industry%3D%26position%3D&s=3&g=&friend_source=0&s=3&friend_source=0; __c=1640673417; __a=58884440.1640673417..1640673417.13.1.13.13; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1641892420; __zp_stoken__=babbdWEltdSRkem9eEUd5MQIjbRgxBmkqYwI7DyNMcjoGMSYSKXkLemwBe0ggO20nNhwPS2R1cVk3V2Q8SnhlcitGLThHPChpUA51c3N6WWhbexI%2FU3pIT1w2EAEkVgQ1dCU9Pz8OBVx1TWE%3D',
'Host': 'www.zhipin.com',
'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': "Windows",
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode':'navigate',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}

keyword='.NET'
url = f'https://www.zhipin.com/job_detail/?query=python&city=101281600&industry=&position='

# res = requests.get(url, headers=headers)
f3 = open("html1.txt","r",encoding='utf-8')  
res = f3.readlines() 

#print(res.content.decode())
html = etree.HTML(res[0])
job_board = html.xpath('//*[@id="main"]//ul/li/div')
parse_list_page(res[0])


print(f"检索到招聘信息：{len(job_board)} 条")
for job_list in job_board:
            list_item = {}
            list_item["title"] = job_list.xpath(".//div[@class=\"job-title\"]//text()")
            # 工作薪资
            list_item["job_salary"] = job_list.xpath(".//div[@class=\"job-limit clearfix\"]/span/text()")
            # 工作年限
            list_item["job_experience"] = job_list.xpath(".//div[@class=\"job-title\"]//text()")
            list_item["tags"] = job_list.xpath(".//div[@class=\"job-title\"]//text()")
            # 公司规模
            list_item["company_scale"] = job_list.xpath(".//div[@class=\"job-title\"]//text()")
            list_item["company_logo"] = job_list.xpath(".//div[@class=\"job-title\"]//text()")
            # 公司所属领域
            list_item["company_industry"] = job_list
    
