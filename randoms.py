
import random
import string

ALL_CHARS = string.digits + string.ascii_letters


def generate_code(code_len=36):
    """生成指定长度的验证码
    
    :param code_len: 验证码的长度(默认4个字符)
    :return: 由大小写英文字母和数字构成的随机验证码字符串
    """
    return ''.join(random.choices(ALL_CHARS, k=code_len))
 

# for _ in range(10):
#     print(generate_code()) 