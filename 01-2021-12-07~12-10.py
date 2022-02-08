# a = int(input('a = '))
# b = int(input('b = '))
# print('%d + %d = %d' % (a, b, a + b))
# print('%d - %d = %d' % (a, b, a - b))
# print('%d * %d = %d' % (a, b, a * b))
# print('%d / %d = %f' % (a, b, a / b))
# print('%d // %d = %d' % (a, b, a // b))
# print('%d %% %d = %d' % (a, b, a % b))
# print('%d ** %d = %d' % (a, b, a ** b))
 
a = 1
b = 2
c= a if a>1 else b #如果a大于1的话，c=a，否则c=b
 
a = 10
b = 3
a += b        # 相当于：a = a + b
a *= a + 2    # 相当于：a = a * (a + 2)
print(a) 


def foo():
    str="function"
    print(str);
if __name__=="__main__":
    print("main")
    foo()
    
    
a = 100
b = 12.345
c = 'hello, world'
d = True
# 整数转成浮点数
print(float(a))    # 100.0
# 浮点型转成字符串 (输出字符串时不会看到引号哟)
print(str(b))      # 12.345
# 字符串转成布尔型 (有内容的字符串都会变成True)
print(bool(c))     # True
# 布尔型转成整数 (True会转成1，False会转成0)
print(int(d))      # 1
# 将整数变成对应的字符 (97刚好对应字符表中的字母a)
print(chr(97))     # a
# 将字符转成整数 (Python中字符和字符串表示法相同)
print(ord('a'))    # 97


print(321 + 123)     # 加法运算
print(321 - 123)     # 减法运算
print(321 * 123)     # 乘法运算
print(321 / 123)     # 除法运算
print(321 % 123)     # 求模运算
print(321 // 123)    # 整除运算
print(321 ** 123)    # 求幂运算

a = 10
b = 3
a += b        # 相当于：a = a + b
a *= a + 2    # 相当于：a = a * (a + 2)
print(a)      # 算一下这里会输出什么


flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)
print('flag0 =', flag0)    # flag0 = True
print('flag1 =', flag1)    # flag1 = True
print('flag2 =', flag2)    # flag2 = False
print('flag3 =', flag3)    # flag3 = False
print('flag4 =', flag4)    # flag4 = True
print('flag5 =', flag5)    # flag5 = False


#x = float(input('x = ',default=3))
x=1
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print(f'f({x}) = {y}')


"""
判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积

Version: 0.1
Author: 骆昊
"""
# a = float(input('a = ',default=3))
# b = float(input('b = ',default=4))
# c = float(input('c = ',default=5))
a =3
b =4
c = 5
if a + b > c and a + c > b and b + c > a:
    peri = a + b + c
    print(f'周长: {peri}')
    half = peri / 2
    area = (half * (half - a) * (half - b) * (half - c)) ** 0.5
    print(f'面积: {area}')
else:
    print('不能构成三角形')
    
    
#循环
num=100
for item in range(1,100):
   num += item
   print(num)   
        
    
    
 
total = 0
for x in range(1, 101):
    total += x
print(total)


# while
# import random 

# # 产生一个1-100范围的随机数
# answer = random.randint(1, 100)
# counter = 0
# while True:
#     counter += 1
#     print(f'目标数字：{answer}')
#     number = int(input('请输入: '))
#     if number < answer:
#         print('大一点')
#     elif number > answer:
#         print('小一点')
#     else:
#         print('恭喜你猜对了!')
#         break
# # 当退出while循环的时候显示用户一共猜了多少次
# print(f'你总共猜了{counter}次')


# var = 5                   
# while var > 0:              
#    var = var -1
#    if var == 3:
#       continue
#    print('当前变量值 :', var)
# print("Good bye!")

# print('qiu 20')
# a, b = 0, 1
# for _ in range(20):
#     a, b = b, a + b
#     print(a)

comedian = {'name': 'Eric Idle', 'age': 74}
print(f"The comedian is {comedian['name']}, aged {comedian['age']}.")


#数据类型
#[]列表 {}集合 ()元组  字典{'Name': 'Zara', 'Age': 7, 'Class': 'First'}


#列表是由一系元素按特定顺序构成的数据序列，
# 这样就意味着定义一个列表类型的变量，
# 可以保存多个数据，而且允许有重复的数据,可变

items1 = [35, 12, 99, 68, 55, 87]
items2 = [45, 8, 29]

# 列表的拼接
items3 = items1 + items2
print(items3)    # [35, 12, 99, 68, 55, 87, 45, 8, 29]

# 列表的重复
items4 = ['hello'] * 3
print(items4)    # ['hello', 'hello', 'hello']

# 列表的成员运算
print(100 in items3)        # False
print('hello' in items4)    # True

# 获取列表的长度(元素个数)
size = len(items3)
print(size)                 # 9

# 列表的索引
print(items3[0], items3[-size])        # 35 35
items3[-1] = 100
print(items3[size - 1], items3[-1])    # 100 100

# 列表的切片
print(items3[:5])          # [35, 12, 99, 68, 55]
print(items3[4:])          # [55, 87, 45, 8, 100]
print(items3[-5:-7:-1])    # [55, 68]
print(items3[::-2])        # [100, 45, 55, 99, 35]

# 列表的比较运算
items5 = [1, 2, 3, 4]
items6 = list(range(1, 5))
# 两个列表比较相等性比的是对应索引位置上的元素是否相等
print(items5 == items6)    # True
items7 = [3, 2, 1]
# 两个列表比较大小比的是对应索引位置上的元素的大小
print(items5 <= items7)    # True






#元组也是多个元素按照一定的顺序构成的序列
# 。元组和列表的不同之处在于，元组是不可变类型，
# 这就意味着元组类型的变量一旦定义，
# 其中的元素不能再添加或删除，而且元素的值也不能进行修改
# 定义一个三元组
t1 = (30, 10, 55)
# 定义一个四元组
t2 = ('骆昊', 40, True, '四川成都')

# 查看变量的类型
print(type(t1), type(t2))    # <class 'tuple'> <class 'tuple'>
# 查看元组中元素的数量
print(len(t1), len(t2))      # 3 4

# 通过索引运算获取元组中的元素
print(t1[0], t1[-3])         # 30 30
print(t2[3], t2[-1])         # 四川成都 四川成都

# 循环遍历元组中的元素
for member in t2:
    print(member)

# 成员运算
print(100 in t1)    # False
print(40 in t2)     # True

# 拼接
t3 = t1 + t2
print(t3)           # (30, 10, 55, '骆昊', 40, True, '四川成都')

# 切片
print(t3[::3])      # (30, '骆昊', '四川成都')

# 比较运算
print(t1 == t3)    # False
print(t1 >= t3)    # False
print(t1 < (30, 11, 55))    # True


#字符串
s1 = '\'hello, world!\''
print(s1)
s2 = '\\hello, world!\\'
print(s2)



 

#字典

aaa=dict(aw='1')
bbb={'key':1}
dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
print(aaa)
print(bbb)
print(dict)
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
 
print ("dict['Name']: "), dict['Name']
print ("dict['Age']: "), dict['Age']

#字符串
s1 = 'hello, world'
print('wo' in s1)    # True
s2 = 'goodbye'
print(s2 in s1)      # False

s = 'abc123456'
N = len(s)

# 获取第一个字符
print(s[0], s[-N])    # a a

# 获取最后一个字符
print(s[N-1], s[-1])  # 6 6

# 获取索引为2或-7的字符
print(s[2], s[-7])    # c c

# 获取索引为5和-4的字符
print(s[5], s[-4])    # 3 3

def fac(num):
    """求阶乘"""
    result = 1
    for n in range(1, num + 1):
        result *= n
    # 返回num的阶乘（因变量）
    return result


m = int(input('m = '))
n = int(input('n = '))
# 当需要计算阶乘的时候不用再写重复的代码而是直接调用函数fac
# 调用函数的语法是在函数名后面跟上圆括号并传入参数
print(fac(m) // fac(n) // fac(m - n))

#函数以及模块

def fabs(num):
    asq = 1
    for item in range(1,num+1):
        asq *= item
        return asq


from random import randint


# 默认值 定义摇色子的函数，n表示色子的个数，默认值为2
def roll_dice(n=2):
    """摇色子返回总的点数"""
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


# 如果没有指定参数，那么n使用默认值2，表示摇两颗色子
print(roll_dice())
# 传入参数3，变量n被赋值为3，表示摇三颗色子获得点数
print(roll_dice(3))




#可变参数
def add(*args):
    total = 0
    # 可变参数可以放在for循环中取出每个参数的值
    for val in args:
        if type(val) in (int, float):
            total += val
    return total


# 在调用add函数时可以传入0个或任意多个参数
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))




def kebian(agrs):
    total=0
    for item in agrs:
        if(type(item) in(int,float)):
           total+=item 
        
    print(total)




import module1
module1.play(1,2,3,4)

from module2 import plays
plays(1,2,3,4,5,5)

import module1 as m1
m1.play(12,12,12,12,12)


from module2 import plays as f2
f2(1,2,3,4,5,6,6)


# bs	返回一个数的绝对值，例如：abs(-1.3)会返回1.3。
# bin	把一个整数转换成以'0b'开头的二进制字符串，例如：bin(123)会返回'0b1111011'。
# chr	将Unicode编码转换成对应的字符，例如：chr(8364)会返回'€'。
# hex	将一个整数转换成以'0x'开头的十六进制字符串，例如：hex(123)会返回'0x7b'。
# input	从输入中读取一行，返回读到的字符串。
# len	获取字符串、列表等的长度。
# max	返回多个参数或一个可迭代对象中的最大值，例如：max(12, 95, 37)会返回95。
# min	返回多个参数或一个可迭代对象中的最小值，例如：min(12, 95, 37)会返回12。
# oct	把一个整数转换成以'0o'开头的八进制字符串，例如：oct(123)会返回'0o173'。
# open	打开一个文件并返回文件对象。
# ord	将字符转换成对应的Unicode编码，例如：ord('€')会返回8364。
# pow	求幂运算，例如：pow(2, 3)会返回8；pow(2, 0.5)会返回1.4142135623730951。
# print	打印输出。
# range	构造一个范围序列，例如：range(100)会产生0到99的整数序列。
# round	按照指定的精度对数值进行四舍五入，例如：round(1.23456, 4)会返回1.2346。
# sum	对一个序列中的项从左到右进行求和运算，例如：sum(range(1, 101))会返回5050。
# type	返回对象的类型，例如：type(10)会返回int；而type('hello')会返回str。


# 标准函数

def get_suffix(filename, ignore_dot=True):
    """获取文件名的后缀名
    
    :param filename: 文件名
    :param ignore_dot: 是否忽略后缀名前面的点
    :return: 文件的后缀名
    """
    # 从字符串中逆向查找.出现的位置
    pos = filename.rfind('.')
    # 通过切片操作从文件名中取出后缀名
    if pos <= 0:
        return ''
    return filename[pos + 1:] if ignore_dot else filename[pos:]


def is_triangle(a, b, c):
    print(f'a = {a}, b = {b}, c = {c}')
    return a + b > c and b + c > a and a + c > b


# 调用函数传入参数不指定参数名按位置对号入座
print(is_triangle(1, 2, 3))
# 调用函数通过“参数名=参数值”的形式按顺序传入参数
print(is_triangle(a=1, b=2, c=3))
# 调用函数通过“参数名=参数值”的形式不按顺序传入参数
print(is_triangle(c=3, a=1, b=2))

#参数*******
def test_kwargs(first, *args, **kwargs):
       print('Required argument: ', first)
       print(type(kwargs))
       for v in args:
          print ('Optional argument (args): ', v)
       for k, v in kwargs.items():
          print ('Optional argument %s (kwargs): %s' % (k, v))

test_kwargs(1, 2, 3, 4, k1=5, k2=6)
#  Required argument:  1
# <class 'dict'>
# Optional argument (args):  2
# Optional argument (args):  3
# Optional argument (args):  4
# Optional argument k2 (kwargs): 6
# Optional argument k1 (kwargs): 5


# 将函数作为参数和调用函数是有显著的区别的
# ，调用函数需要在函数名后面跟上圆括号，
# 而把函数作为参数时只需要函数名即可


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
print(calc(1, 2, x=3, y=4, z=5, init_value=1, op=operator.mul)) 




#高阶函数 map
# map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，
# 并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。
 


def f(x):
    return x*x
aas=[1, 2, 3, 4, 5, 6, 7, 8, 9]
r=map(f, aas)
print(list(r)) 


numbers1 = [35, 12, 8, 99, 60, 52]
numbers2 = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers1)))
print(numbers2)  
 
def sum(x,y):
      return x+y
 
 
#filter
# Python内建的filter()函数用于过滤序列。

# 和map()类似，filter()也接收一个函数和一个序列。
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素。
 
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# 结果: [1, 5, 9, 15]
 
#reduce
# 再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算，其效果就是：




#lambda
qw=lambda sq,we:sq+we

print(qw(1,2))

p = lambda x,y:x+y
print(p(4,6))
 

 

a=lambda x:x*x
print(a(3))       # 注意：这里直接a(3)可以执行，但没有输出的，前面的print不能少 
 
 

a = lambda x,y,z:(x+8)*y-z
print(a(5,6,8))


#调用函数需要在函数名后面跟上圆括号，而把函数作为参数时只需要函数名即可。
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


#面向对象
class Student:
    """学生"""

    def __init__(self, name, age):
        """初始化方法"""
        self.name = name
        self.age = age

    def study(self, course_name):
        """学习"""
        print(f'{self.name}正在学习{course_name}.')

    def play(self):
        """玩耍"""
        print(f'{self.name}正在玩游戏.')

stu1 = Student('骆昊', 40)
print(stu1)        # 骆昊: 40
students = [stu1, Student('李元芳', 36), Student('王大锤', 25)]
print(students)    # [骆昊: 40, 李元芳: 36, 王大锤: 25]


#动态属性
class Student:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student('王大锤', 20)
# 为Student对象动态添加sex属性
stu.sex = '男'

# 私有属性
# 在实际项目开发中，我们并不经常使用私有属性，
# 属性装饰器的使用也比较少，
# 所以上面的知识点大家简单了解一下就可以了。
class Student:
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # 属性访问器(getter方法) - 获取__name属性
    @property
    def name(self):
        return self.__name
    
    # 属性修改器(setter方法) - 修改__name属性
    @name.setter
    def name(self, name):
        # 如果name参数不为空就赋值给对象的__name属性
        # 否则将__name属性赋值为'无名氏'，有两种写法
        # self.__name = name if name else '无名氏'
        self.__name = name or '无名氏'
    
    @property
    def age(self):
        return self.__age


stu = Student('王大锤', 20)
print(stu.name, stu.age)    # 王大锤 20
stu.name = ''
print(stu.name)    # 无名氏
# stu.age = 30     # AttributeE




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


Triangle.is_valid(3,4,5)



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
teacher.teach('Python程序设计')
stu1.study('Python程序设计')


example_list = [
    {'points': 400, 'gold': 2480},
    {'points': 100, 'gold': 610},
    {'points': 100, 'gold': 620},
    {'points': 100, 'gold': 620}
]

total_gold = 0
for item in example_list:
    total_gold += example_list["gold"]
    
 
sum(item['gold'] for item in example_list)

#encoding:UTF-8
def foo(num):
    for i in num:
        yield i
        print('end'+str(i))
num=[1, 2, 3, 4, 5]
demo = foo(num)
#next()返回迭代器的下一个项目（项目在本示例是一个数值）1
print(next(demo))
print("*"*20)
print(next(demo))
print("*"*20)
print(next(demo))
'''返回值：
1
********************
end1
2
********************
end2
3
'''
# yield相当于一个迭代生成器。带有yield的函数是迭代函数，返回一个可迭代对象；
# 在遍历其部分迭代项目时，获取下一个项目会沿着上一次yield截止处，
# 继续运行同级代码后，再重头运行函数；yield后的不同级代码只有获取最后一个项目后运行。


