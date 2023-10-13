import requests

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://bfweb.hk.beanfun.com',
    'Referer': 'https://bfweb.hk.beanfun.com/member/forgot_pwd.aspx',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
  '__EVENTTARGET': '',
  '__EVENTARGUMENT': '',
  '__VIEWSTATE': 'r9lUVAWAgwntRj9rHhif4XeXUbl+BUR+uIGeoegkUDC1jG+t9Jn35LemYkZ5Gye3J+nudASiGb9l4W+wfbWwz1AbULZsxPGaYE6miWY6yowqVRtMVZ50vWP1t6Jdc/bEWyy0Q4R+3pvZZripuDh5dvfBbDOKZn8jYNMaZM9CILoeAQ3pgxTA3j153e/Y5+40D3Tvn19zBCF2obC0cQRqSkZWQ04qwTNwLna8ktzcYsmyAxniVOYjunw1ShhQAFd0F5ngRmEuV4LEB8XuJhsEwnuaCzZ4CE2WlQxqlYjEbEbbvtkNeyefE/xN53rxw0p1qB6vX19Hbwr70y9xLSv28RA370H4yXX9cx5ZlJKy1oRTxQEv3hcZpTK7smdhyVD5hHNazh+LTn5pcTjTxzxijq5FgYhUKLbofnDw4mVg+M3znbSK57BG10BKQrHjXuTbf59dxrCIeH71b8nxFj/WkLcx5cfhvZbLCQA7wEVOaTfYStLgNl9j9kUGnaGPgCaRrbyJup3x5KyCteMXDReay6mAisNbSss/pvW2bF9IE/VmlQocLvvurRSvoidcSC4ygZQ8LbZALpz4Sg95/4/4KSlyZQ6jHQ6gXuDY7C4BphM8BddEsJdJ7FfcUe67koh8gvqcjo/y1VPty4+XN9ww+uCxVg7fcPeuGK74whk+BpCNJfbX+7YtDy7UCJhcfkDZuQPS0QE0J9JYN3xGa277NLK6eF+dJmYZ6uan8IUf4UglcEQwIhTNqCdCOET2YM7AXQLXarrc54OVcvlwH3LUiSmBmsj9JJnONtruhH4u73cwsIGNPsxcex8e06YiAc/v6J6dBeB4UDQb3c1UUgnshKc3xzVY1fb90WJN/NGYytznDjlWyZyERv94IyhDMcgECPR3xtkR8BtvUmOCProEmykPFjOVw8xEew/KC2GKiLKkb7qWUaH5eMApD7pQ/+4XyUqI76ZCT/iBOVFvGECLQ1GI4epyZWORO+1v1LTLY6bKJxzgeakWskXbntvi522Qk0p4ZO0Tq/zwyO+AcjAACRWPUu4j3SrKCpGevNPjE9y9h/1HHKEfKXy8WA/p+Edy5ln4WYqKMHbarokg+t2Szs+s9Y+CCZfBh6eSPbB+AzDB/btqBygUHLfO2FXYj7Sb9axUse34d+DapkXia3OyqwB1iZt0Oh+4t+4vs80V7dbzB8LJ1+4O8StuBbjT2TkdfmRo5kH7X7PUUpkxFlxaewBHWYsJ5jWoOnXqSctbK1X76zmhTRMF6ruoYk+b7pO2Mb+N5rhUizjv25gPUP+siFyImBWhECAC9jumG8JnEopy1TR8mJu9FouoFwLm7M/Y1VRhNpY7N6lALc86+e1PAKcXcWal+SV5y9ktGyMbN4vk1H0S8EQLiuCfQECGm42mFe/l9z9UAzvlltAetI+DV9qji6lo7UsP4rcGxjpzU1jBr69KmogPrRg48EFN7fpAUalc6wD4tFu9WQ1ieRamywOawg0eX3ev0kF+pUO6We+cy5TebZF5JuDTDknE03Y88Rtqrsoq6Uv0hrzPgXAKM8h4RrpvQZ5Eu2Kg02hZHzJDlXvHY1m0/uwO0MyYGYQFdQ5+/tY2rzTt7i5Ky75u8uP43NFfMPGavL8eUi1wWUd3oPXx75Od5UNnWZTpLeXC8+jFDFe4QZzKkUM5exGEO1pk8deATMWkcbBptSBjN7N0IM+KR8TPsPmJmvieUhzvIL/uA/F7hoMZsDtQ/gI8hsNhcVUpaUIR1AhQqxVewd8/f9rT',
  '__VIEWSTATEGENERATOR': '0B39EC19',
  '__VIEWSTATEENCRYPTED': '',
  '__EVENTVALIDATION': 'qlFG1qdhco2LoipUntJx/mwhTbBTzJzItmgayhzrY5WTclyeDacuq/9CI2dfUdKPqNfGxrsHywGNP7OlkuzItF4YEOiLGXRXgTHyI+w+cB92i3UKiqRZ2IE7NPnrZI+DbjoNWRhBbhT/okwsebKi7shmR1DFycHRfsMQy+6Wnk7lIIEv',
  'ctl00$ContentPlaceHolder1$q_type': '1',
  'ctl00$ContentPlaceHolder1$t_email': 'LJBAFLAKADH@bfhappy.com',
  'ctl00$ContentPlaceHolder1$AreaList': '',
  'ctl00$ContentPlaceHolder1$t_phone': '',
  'ctl00$ContentPlaceHolder1$t_account': '',
  'g-recaptcha-response': '',
  'ctl00$ContentPlaceHolder1$Button1': '\u9001\u51FA\u67E5\u8A62',
  'ctl00$ContentPlaceHolder1$token1': ''
}

data2 = {
  '__EVENTTARGET': '',
  '__EVENTARGUMENT': '',
  '__VIEWSTATE': 'r9lUVAWAgwntRj9rHhif4XeXUbl+BUR+uIGeoegkUDC1jG+t9Jn35LemYkZ5Gye3J+nudASiGb9l4W+wfbWwz1AbULZsxPGaYE6miWY6yowqVRtMVZ50vWP1t6Jdc/bEWyy0Q4R+3pvZZripuDh5dvfBbDOKZn8jYNMaZM9CILoeAQ3pgxTA3j153e/Y5+40D3Tvn19zBCF2obC0cQRqSkZWQ04qwTNwLna8ktzcYsmyAxniVOYjunw1ShhQAFd0F5ngRmEuV4LEB8XuJhsEwnuaCzZ4CE2WlQxqlYjEbEbbvtkNeyefE/xN53rxw0p1qB6vX19Hbwr70y9xLSv28RA370H4yXX9cx5ZlJKy1oRTxQEv3hcZpTK7smdhyVD5hHNazh+LTn5pcTjTxzxijq5FgYhUKLbofnDw4mVg+M3znbSK57BG10BKQrHjXuTbf59dxrCIeH71b8nxFj/WkLcx5cfhvZbLCQA7wEVOaTfYStLgNl9j9kUGnaGPgCaRrbyJup3x5KyCteMXDReay6mAisNbSss/pvW2bF9IE/VmlQocLvvurRSvoidcSC4ygZQ8LbZALpz4Sg95/4/4KSlyZQ6jHQ6gXuDY7C4BphM8BddEsJdJ7FfcUe67koh8gvqcjo/y1VPty4+XN9ww+uCxVg7fcPeuGK74whk+BpCNJfbX+7YtDy7UCJhcfkDZuQPS0QE0J9JYN3xGa277NLK6eF+dJmYZ6uan8IUf4UglcEQwIhTNqCdCOET2YM7AXQLXarrc54OVcvlwH3LUiSmBmsj9JJnONtruhH4u73cwsIGNPsxcex8e06YiAc/v6J6dBeB4UDQb3c1UUgnshKc3xzVY1fb90WJN/NGYytznDjlWyZyERv94IyhDMcgECPR3xtkR8BtvUmOCProEmykPFjOVw8xEew/KC2GKiLKkb7qWUaH5eMApD7pQ/+4XyUqI76ZCT/iBOVFvGECLQ1GI4epyZWORO+1v1LTLY6bKJxzgeakWskXbntvi522Qk0p4ZO0Tq/zwyO+AcjAACRWPUu4j3SrKCpGevNPjE9y9h/1HHKEfKXy8WA/p+Edy5ln4WYqKMHbarokg+t2Szs+s9Y+CCZfBh6eSPbB+AzDB/btqBygUHLfO2FXYj7Sb9axUse34d+DapkXia3OyqwB1iZt0Oh+4t+4vs80V7dbzB8LJ1+4O8StuBbjT2TkdfmRo5kH7X7PUUpkxFlxaewBHWYsJ5jWoOnXqSctbK1X76zmhTRMF6ruoYk+b7pO2Mb+N5rhUizjv25gPUP+siFyImBWhECAC9jumG8JnEopy1TR8mJu9FouoFwLm7M/Y1VRhNpY7N6lALc86+e1PAKcXcWal+SV5y9ktGyMbN4vk1H0S8EQLiuCfQECGm42mFe/l9z9UAzvlltAetI+DV9qji6lo7UsP4rcGxjpzU1jBr69KmogPrRg48EFN7fpAUalc6wD4tFu9WQ1ieRamywOawg0eX3ev0kF+pUO6We+cy5TebZF5JuDTDknE03Y88Rtqrsoq6Uv0hrzPgXAKM8h4RrpvQZ5Eu2Kg02hZHzJDlXvHY1m0/uwO0MyYGYQFdQ5+/tY2rzTt7i5Ky75u8uP43NFfMPGavL8eUi1wWUd3oPXx75Od5UNnWZTpLeXC8+jFDFe4QZzKkUM5exGEO1pk8deATMWkcbBptSBjN7N0IM+KR8TPsPmJmvieUhzvIL/uA/F7hoMZsDtQ/gI8hsNhcVUpaUIR1AhQqxVewd8/f9rT',
  '__VIEWSTATEGENERATOR': '0B39EC19',
  '__VIEWSTATEENCRYPTED': '',
  '__EVENTVALIDATION': 'qlFG1qdhco2LoipUntJx/mwhTbBTzJzItmgayhzrY5WTclyeDacuq/9CI2dfUdKPqNfGxrsHywGNP7OlkuzItF4YEOiLGXRXgTHyI+w+cB92i3UKiqRZ2IE7NPnrZI+DbjoNWRhBbhT/okwsebKi7shmR1DFycHRfsMQy+6Wnk7lIIEv',
  'ctl00$ContentPlaceHolder1$q_type': '1',
  'ctl00$ContentPlaceHolder1$t_email': 'MWYBTAMBTL@bfhappy.com',
  'ctl00$ContentPlaceHolder1$AreaList': '',
  'ctl00$ContentPlaceHolder1$t_phone': '',
  'ctl00$ContentPlaceHolder1$t_account': '',
  'g-recaptcha-response': '',
  'ctl00$ContentPlaceHolder1$Button1': '\u9001\u51FA\u67E5\u8A62',
  'ctl00$ContentPlaceHolder1$token1': ''
}

proxy = {
    'http': '10.0.128.253:4443',
    'https': '10.0.128.253:4443',
}

def call_api():
                response = requests.post('https://bfweb.hk.beanfun.com/member/forgot_pwd.aspx', headers=headers, data=data,proxies=proxy)
                responses = requests.post('https://bfweb.hk.beanfun.com/member/forgot_pwd.aspx', headers=headers, data=data2,proxies=proxy)
                print("response开始\n")
                print(response.text)
                print("response结束\n")
                print("responses开始\n")
                print(responses.text)
                print("responses结束\n")
                 
while True:
    call_api()
    time.sleep(900)  # 等待15分钟

 
