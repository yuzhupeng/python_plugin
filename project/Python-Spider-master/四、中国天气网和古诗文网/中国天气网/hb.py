
import requests
from bs4 import BeautifulSoup

def parse_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
    }
    response = requests.get(url)
    text = response.content.decode('utf-8')
    soup = BeautifulSoup(text,'lxml')
    conMidtab = soup.find('div',class_='conMidtab')
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        for tr in trs:
            tds = tr.find_all('td')
            city_td = tds[0]
            #stripped_strings发返回的是生成器，所以先变成列表，再去第0个
            city = list(city_td.stripped_strings)[0]
            temp_td = tds[-2]
            temp = list(temp_td.stripped_strings)[0]
            print({'city':city,'temp':temp})

def main():
    url = 'http://www.weather.com.cn/textFC/hb.shtml'
    parse_page(url)

if __name__ == '__main__':
    main()