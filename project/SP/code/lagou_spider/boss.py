import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Host': 'www.zhipin.com',
    'Cookie': 'lastCity=101250100; wd_guid=bc56fff1-0618-4bda-a23a-40e31ee02bd6; historyState=state; wt2=DfpTM8emYL9l2HQbSML_Xgo4j1gEikRu9ECszaHu5Hmf4Xw6d8i5fK8ggH2zTfI5AOUUKe-1SxELfgqrZVVE8Ig~~; _bl_uid=Rjkbgwmaom8eXj1gLdFbeFb1y9qb; acw_tc=0bccaf0a16388418068142548e07e4b80fc9fe6e55bae7b435ac021f6a6af5; sid=sem; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1638414709,1638841816; __zp_seo_uuid__=b3f26e3a-d726-4dbb-8c3b-fed0e1df3c52; __l=r=https%3A%2F%2Fwww.zhipin.com%2Fweb%2Fcommon%2Fsecurity-check.html%3Fseed%3DPzBL753jgNx4KP3JsvQgayYdrC%252BS4jR9FQqH6fYVIss%253D%26name%3D388b5360%26ts%3D1638841816932%26callbackUrl%3Dhttps%253A%252F%252Fwww.zhipin.com%252Fchangsha%252F%253Fkeyword%253D26126832%2526bd_vid%253D11597564925484946276%2526sid%253Dsem%2526_ts%253D1638841806833&l=%2Fcitysite%2Fchangsha%2F%3Fkeyword%3D26126832%26bd_vid%3D11597564925484946276%26sid%3Dsem%26_ts%3D1638841806833&s=1; __g=sem; __c=1638841816; __a=41905189.1638414708.1638414708.1638841816.29.2.8.8; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1638842441; __zp_stoken__=7f80dZ1Z4THYlRGlmXkUGP38UU3UtYV53YBFsJXA6X2E%2FSS4%2BA2xXDX9%2Fcy1UNT5yGh9NKEd7GAZ6CW0ALTEPdHJjLHwtDzEdQhw0TxBYPyxOeA8sN2NzZGViRANcFns%2FWCZ%2FAEcAZwM4Rx0%3D; geek_zp_token=V1QtskE-H62FpgXdNqxxUcKiK07jvQzQ~~'
}

url = 'https://www.zhipin.com/c101250100-p100109/?page=1&ka=page-1'

res = requests.get(url, headers=headers)
print(res.content.decode())
html = etree.HTML(res.text)
ul_list = html.xpath('//*[@id="main"]/div/div[3]/ul')[0]
for li in ul_list:
    params = {}
    params["job_name"] = li.xpath('./span[@class="job_name"]/a/text()')[0]
    print(params)
