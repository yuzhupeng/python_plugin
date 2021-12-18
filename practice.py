print(repr(1))




applyno='{[199992]'
applyno=applyno.replace('[','')
applyno=applyno.replace(']','')
print(applyno)
a='SELECT count(*) FROM CasTravel WHERE BwfTravelNo=%s', applyno

applyno='1'
sql=f'SELECT count(*) FROM CasTravel WHERE BwfTravelNo=\'{applyno}\''
print(sql)

import os.path
import sys


path = os.path.realpath(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(path)))







a= not True




value_titleS=[["申请单号","实际使用者","用车日期","行程"]]
 
 




newlist3=[" "]
f3 = open("html.txt","r",encoding='utf-8')  
original_list3 = f3.readlines()       #读取全部内容 ，并以列表方式返回 
for i in original_list3:          #遍历去重
  if not i in newlist3:
      newlist3.append(i)
newtxt3="".join(newlist3)
 
for item in newlist3:
    sts="".join(item)
    sss=len(sts.strip())
    if sss>0 and sss!=15:
       str_to_dict = eval(sts)
       applyno=str_to_dict['applyno']
       AcutalUser=str_to_dict['AcutalUser']
       usedate=str_to_dict['TravelDetial'][0]['usedate']
       travel=str_to_dict['TravelDetial'][0]['travel']
       op=[]
       op.append(applyno)
       op.append(AcutalUser)
       op.append(usedate)
       op.append(travel)
       value_titleS.append(op)






value_title = [["姓名", "性别", "年龄", "城市", "职业"],
          ["111", "女", "66", "石家庄", "运维工程师"],
          ["222", "男", "55", "南京", "饭店老板"],
          ["333", "女", "27", "苏州", "保安"]]



 
       

 


import xlwt
 
def write_excel_xls(path, sheet_name, value):
    index = len(value)  # 获取需要写入数据的行数(value是个二维数组)
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
    workbook.save(path)  # 保存工作簿
    print("xls格式表格写入数据成功！")
 
# 保存到当前工程目录
book_name_xls = 'test.xls'
 
sheet_name_xls = 'xls格式测试表'
 
value_title = [["姓名", "性别", "年龄", "城市", "职业"],
          ["111", "女", "66", "石家庄", "运维工程师"],
          ["222", "男", "55", "南京", "饭店老板"],
          ["333", "女", "27", "苏州", "保安"]]
 
write_excel_xls(book_name_xls, sheet_name_xls, value_titleS)
  
  
  
  
 

RES={"applyno": "GA03-202111-47026", "bwfstatus": "完成", "AcutalUser": "黄玉娴1人", "InSideLine": "1592", "Company": "skc", "applytype": "新申请", "reason": "新申请不需要填写（新規申請の場合は記入不要）", "userason": "事务处理", "DetailedAddress": "SKC-KDTCN", "PhonePassenger": "15989191796", "ShareCore": "15700", "CostDepartment": "KCSS", "applyperson": "姚 青", "applydate": "2021/11/25", "createtime": "2021-12-16 16:54:30", "TravelDetial": [{"usedate": "2021/11/26", "travel": "SKC-KDTCN", "OstartTime": "  08:30", "ReturnTime": "  09:30", "FlightNo": "", "FlightTime": "  :"}]}

applyno=RES['applyno']
AcutalUser=RES['AcutalUser']
usedate=RES['TravelDetial'][0]['usedate']
travel=RES['TravelDetial'][0]['travel']

import uuid
  
print(uuid.uuid1())
print(uuid.uuid1())

 



my_dict = {
    'name': '112222-1222-1-1-2v',
    'names': '2012-44-11',
    'age': 40,
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}
print(my_dict['name']+my_dict['names'])





import pyslserver

sqlhelper=pyslserver.HandCost('.','sa','1','Skc_Business')
sqlhelper.aaaa('222222')
sqlhelper.dictToTO('detial')












import uuid
  
print(uuid.uuid1())
print(uuid.uuid1())


import time
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 写文件

import csv
import datetime

csv.register_dialect(
    "mydialect",
    delimiter=',',              # 字段分隔符
    escapechar='\\',            # 转义字符
    quotechar='"',              # 包裹字符
    doublequote=False,          # 使转义字符生效
    lineterminator='\n',        # 行与行之间的分隔符
    quoting=csv.QUOTE_ALL       # 包裹模式
)
data = [
    [1, "a,bc", 19.353, datetime.datetime(2001, 3, 17)],
    [2, "ei,f", 13.287, datetime.datetime(2011, 4, 27)],
    [3, 'q"ij', 15.852, datetime.datetime(2003, 7, 14)],
    [4, "zh'n", 11.937, datetime.datetime(2012, 1, 9)],
    [5, "i'op", 12.057, datetime.datetime(2009, 5, 18)],
]
with open("test.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=["id", "name", "float", "datetime"], dialect="excel")
    writer.writeheader()
    for item in data:
        writer.writerow(item)








#继承和多肽
class Person:
    """人类"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f'{self.name}正在吃饭.')
    
    def sleep(self):
        print(f'{self.name}正在睡觉.')


class Student(Person):
    """学生类"""
    
    def __init__(self, name, age):
        # super(Student, self).__init__(name, age)
        super().__init__(name, age)
    
    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}.')


class Teacher(Person):
    """老师类"""

    def __init__(self, name, age, title):
        # super(Teacher, self).__init__(name, age)
        super().__init__(name, age)
        self.title = title
    
    def teach(self, course_name):
        print(f'{self.name}{self.title}正在讲授{course_name}.')



stu1 = Student('白元芳', 21)
stu2 = Student('狄仁杰', 22)
teacher = Teacher('武则天', 35, '副教授')
stu1.eat()
stu2.sleep()
teacher.eat()
teacher.teach('Python程序设计')
stu1.study('Python程序设计')






#静态方法
class Triangle(object):
    """三角形类"""

    def __init__(self, a, b, c):
        """初始化方法"""
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        """判断三条边长能否构成三角形(静态方法)"""
        return a + b > c and b + c > a and a + c > b

    # @classmethod
    # def is_valid(cls, a, b, c):
    #     """判断三条边长能否构成三角形(类方法)"""
    #     return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c

    def area(self):
        """计算面积"""
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


print(Triangle.is_valid(3,4,5))












from logging import exception
import sc.log4 
log = sc.log4.get_logger()

try:
    f=open("d:\\abc.txt")
except BaseException as msg:
    print(f'cc{msg}')
    log.error(f"request获取明细信息出错 ：Unexpected Error: {msg}")
 


import operator
def calc(*args, **kwargs):
    result = 0
    for arg in args:
        if type(arg) in (int, float):
            result += arg
    for value in kwargs.values():
        if type(value) in (int, float):
            result += value
    return result

# print(calc(1, 2, 3, init_value=0, op=operator.add, x=4, y=5))      # 15
print(calc(1, 2, x=3, y=4, z=5, init_value=1, op=operator.mul))    # 16

import base64
import uuid
  
print(uuid.uuid1())
# get a UUID - URL safe, Base64

 
def f(x):
        return x+x

 
aas=[1,2,3,3,2,2,2,2,2,2,2,1,2,2]
r=map(f, aas)
print(list(r)) 


from functools import reduce
def add_2(x, y):
    return x+y
a7 = map(add_2, [1,2,3,3,2,2,2,2,2,2,2,1,2,2])  #得到的是一个值，依次执行add_2(1,2)，对结果和3执行add_2(add_2(1,2),3)，有点类似递归运算
print(a7) 
 
 
 
print(uuid.uuid1())
 

asq=[]

for item in range(1,6): 
    asq.append(item)
 
 
print(asq)
 
def fac(num):
    if num in (0, 1):
        return 1
    return num * fac(num - 1)

print(fac(10))


numbers1 = [35, 12, 8, 99, 60, 52]
numbers2 = list(map(lambda x: x ** 5, filter(lambda x: x % 2 == 0, numbers1)))
print(numbers2) 

print('1')

def sum(x,y):
      return x+y
 

 

p = lambda x,y:x+y
print(p(4,6))
 

 

a=lambda x:x*x
print(a(3))       # 注意：这里直接a(3)可以执行，但没有输出的，前面的print不能少 
 
 

a = lambda x,y,z:(x+8)*y-z
print(a(5,6,8))





def f(x):
    return x*x

 
aas=[1, 2, 3, 4, 5, 6, 7, 8, 9]
r=map(f, aas)
print(list(r)) 

 
 

def is_even(num):
    return num % 2 == 0


def square(num):
    return num ** 2


numbers1 = [35, 12, 8, 99, 60, 52]
numbers2 = list(map(square, filter(is_even, numbers1)))
print(numbers2)    # [144, 64, 3600, 2704]




def test_kwargs(first, *args, **kwargs):
       print('Required argument: ', first)
       print(type(kwargs))
       for v in args:
          print ('Optional argument (args): ', v)
       for k, v in kwargs.items():
          print ('Optional argument %s (kwargs): %s' % (k, v))

test_kwargs(1, 2, 3, 4, k1=5, k2=6)
 







def calc(*args,**a2s):
    result = 0
    for arg in args:
        if type(arg) in (int, float):
            result += arg
    for value in a2s.values():
            if type(value) in (int, float):
              result += value
    return result


print(calc(a=1, b=2, c=3))


def calc(*args,**kwargs):
    result = 0
    for arg in args:
        if type(arg) in (int, float):
            result += arg
    for value in kwargs.values():
        if type(value) in (int, float):
            result += value
    return result


print(calc())                  # 0
print(calc(1, 2, 3))           # 6
print(calc(a=1, b=2, c=3))     # 6
print(calc(1, 2, c=3, d=4))    # 10




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

 
 