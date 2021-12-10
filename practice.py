import re
string = 'abe(ac)ad)'
p1 = re.compile(r'[(](.*?)[)]', re.S) #最小匹配
p2 = re.compile(r'[(](.*)[)]', re.S)  #贪婪匹配
asd=re.findall(p1, string)
asd = asd[0].replace('[','').replace(']','')
print(asd)
print(re.findall(p2, string))
 
phone = "2004-959-559 # 这是一个国外电话号码"
 
# 删除字符串中的 Python注释 
num = re.sub(r'#.*$', "", phone)
print(f"电话号码是: {num}"), num
 
# 删除非数字(-)的字符串 
num = re.sub(r'\D', "", phone)
print(f"电话号码是: {num}"), num


str = 'javaScript:fgoDispForm(296585)'



# pattern = r"\(.*?\)";
# guid = re.findall(pattern,str ,re.M)

guid=re.findall(r'(?: re)',str)
 
print(guid)
if(len(guid)>0):
   guid = guid[0]
   guid = guid.replace('[','').replace(']','')
print(guid)



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

 
 