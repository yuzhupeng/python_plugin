 

from bs4 import BeautifulSoup

a = '''
<body>
    <h><a href='www.biaoti.com'>标题</a></h>
    <p>段落1</p>
    <p></p>
</body>
'''
soup = BeautifulSoup(a, 'html.parser')
for i in soup.body.find_all(True):
    print(i.name) # 提取标签名
    print(i.attrs) # 提取标签所有属性值
    print(i.has_attr('href')) # 检查标签是否有某属性

 
 