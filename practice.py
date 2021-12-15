

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

 
 