import requests
import time


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    # 'referer': 'https://www.lagou.com/wn/jobs?px=new&pn=2&kd=Python&city=%E5%85%A8%E5%9B%BD',
    # 'cookie': 'JSESSIONID=ABAAAECAAEBABIIDC84F57833F5007E349BCA3B61534C02; WEBTJ-ID=20211206192538-17d8f7dfe2c486-01cf3c62eb9efc-b7a1438-2073600-17d8f7dfe2eddf; RECOMMEND_TIP=true; X_HTTP_TOKEN=42daf4b72327b2810499878361bf5e71415983ed09; privacyPolicyPopup=false; user_trace_token=20211206192540-d9ae1a74-106b-4a65-aec1-e5b34c90b14a; LGUID=20211206192540-ce129f60-911f-40aa-8da7-bf61c8aefce8; _ga=GA1.2.268447464.1638789939; _gid=GA1.2.1012016275.1638789939; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1638789939; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1638789939; sensorsdata2015session=%7B%7D; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_navigation; LGRID=20211206192554-11ffeff9-4b4c-4929-a452-416072c95c21; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217d8f7dffc67c6-05ab1c4318a9f4-b7a1438-2073600-17d8f7dffc7cdc%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2294.0.4606.81%22%7D%2C%22%24device_id%22%3A%2217d8f7dffc67c6-05ab1c4318a9f4-b7a1438-2073600-17d8f7dffc7cdc%22%7D'
}

url = 'https://www.lagou.com/jobs/v2/positionAjax.json'

data = {
    'first': 'true',
    'needAddtionalResult': 'false',
    'city': '深圳',
    'px': 'new',
    'kd': '.net'
}

for x in range(1, 10):
    data['pn'] = x
    response = requests.post(url, headers=headers, data=data)
    positions = response.json()["content"]["positionResult"]["result"]
    result_list = []
    for position in positions:
        params = {"positionName": position["positionName"],
                  "companyShortName": position["companyShortName"],
                  "companySize": position["companySize"],
                  "financeStage": position["financeStage"]
                  }
        result_list.append(params)
    print(result_list)
