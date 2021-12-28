import re
import datetime, time

# text = "13348685262"


# ret = re.match('h', text)

# ret = re.match('.', text)
# ret = re.match('\d', text)
# ret = re.match('\D', text)
# ret = re.match('\s', text)
# ret = re.match('\w', text)
# ret = re.match('.', text)
# ret = re.match('[\d\W]*', text)
# ret = re.match('\d*', text)
# ret = re.match('\d+', text)
# ret = re.match('\d{3}', text)
# ret = re.match('\d{1,6}', text)

# 验证是否是手机号码，手机号码的规则是以1开头，第二位是可以3456789，后面9位随意，但必须是数字，一共11位
# text = "13348685262"
# ret = re.match('1[3-9]\d{9}', text)

# # 验证邮箱：邮箱的规则是邮箱名称是用数字、数字、下划线组成的，然后是@符号，后面就是域名了。示例代码如下：
# text = "xiahaoxuan6@gmail.com"
# ret = re.match('\w+@[a-zA-\.]+', text)

# # 验证URL：URL的规则是前面是http或者https或者是ftp然后再加上一个冒号，再加上一个斜杠，再后面就是可以出现任意非空白字符了。示例代码如下：
# text = "http://www.baidu.com"
# ret = re.match('(http|https|ftp)://[^\s]+', text)

# 验证身份证：身份证的规则是，总共有18位，前面17位都是数字，后面一位可以是数字，也可以是小写的x，也可以是大写的X。示例代码如下：

# text = "430421199406280052"
# ret = re.match('^\d{17}(x|X|\d)$', text)

# 匹配0-100之间的数字
# text = "10"
# ret = re.search('0$|[1-9]{2}$|100$', text)
# text = "apple \c"
# ret = re.search(r'\\c',text)
# group = ret.group()
#
# print(group)
timestamp = int(time.mktime(datetime.date.today().timetuple()))



# 例1：北美地区的电话号
#
#     编码方案：电话号码有一个3位数的区号和一位7位数的号码组成(这个7位数有分成  一个3位的局号和一个4位的路号，局号和路号之间使用连字符分隔)
#     每位电话号码可以是任意数字，但是区号和局号的第一位数字不能是0或1.实际书写号码是往往会把区号写在括号里面，或者将区号使用连字符和后面的局号连接起来。
#     例如：（555）123-2234或555-123-1234，有时候在括号你里面会包含空格。例如：（555 ）123-1234
# text = '555-223-1234'
# ret = re.search(r'\（?[2-9]\d{2}\s?\）?-?[2-9]\d{2}-\d{4}$', text)
#
# group = ret.group()
# print(group)

# 例4：中国邮政编码
#
#     我国邮政编码的规则是，前两位是省市自治区，第三位代表邮区，第四位代表县市，最后两位代表投递邮局，总共6为数字。其中第二位不为8(港澳前两位为99，其余为0-7)
text = '991200'
ret = re.search(r'(^\d[0-79]\d{4}$)|(^99[0-7]{4}$)', text)

group = ret.group()
print(group)



