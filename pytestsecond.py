''' try:
    num = int(input("请输入一个整数: "))
    print("你输入的整数是:", num)
except ValueError:
    print("无效的输入，请输入一个整数") '''
 
# import os

# # 源文件路径
# source_file = "path/to/source_file.txt"

# # 临时文件路径
# temp_file = "path/to/temp_file.txt"

# # 文件交换
# with open(source_file, "rt") as file, open(temp_file, "wt") as temp:
#     content = file.read()
#     temp.write(content)

# # 删除源文件
# os.remove(source_file)

# # 重命名临时文件为源文件
# os.rename(temp_file, source_file)


#可变参数
def add(*numbers):
    result = 0
    for num in numbers:
        result += num
    return result

sum1 = add(1, 2, 3)  # 调用函数，传递3个参数
sum2 = add(1, 2, 3, 4, 5)  # 调用函数，传递5个参数
print(sum1)  # 输出 6
print(sum2)  # 输出 15

#默认参数


def power(x, n=2):
    return x ** n

result1 = power(2)  # 调用函数，n使用默认值2
result2 = power(2, 3)  # 调用函数，指定n为3
print(result1)  # 输出 4
print(result2)  # 输出 8


 

#关键字参数
def person_info(**info):
    for key, value in info.items():
        print(key + ": " + value)

person_info(name="Alice", age="25", city="New York")  # 调用函数，传递关键字参数



#返回值
def calculate(a, b):
    sum = a + b
    difference = a - b
    return sum, difference

result1, result2 = calculate(8, 3)
print(result1)  # 输出 11
print(result2)  # 输出 5


# #内置函数 range
# ''' range(start, stop, step)：
# range函数用于生成一个整数序列，可以用来遍历数字范围。
# 它接受三个参数：起始值（可选，默认为0），结束值（必选）
# ，步长（可选，默认为1）。返回的对象是一个可迭代的序列。 '''
# for i in range(0,222,1):
#    print(i)
   
   

   
#    aa=input("1111")

import asyncio
for i in range(0, 222, 1):
        print(i)
def my_async_function():
    
    aa =   asyncio.get_event_loop().run_in_executor(None, input, "请输入与当前数字相关的信息：")
    print("用户输入:", aa)

(my_async_function())