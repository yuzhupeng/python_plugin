import ctypes

# 定义常量
VK_LEFT = 0x25

# 调用GetAsyncKeyState函数
def is_left_arrow_pressed():
    print(ctypes.windll.user32.GetAsyncKeyState(VK_LEFT))
    return ctypes.windll.user32.GetAsyncKeyState(VK_LEFT) < 0

# 测试
while True:
    if is_left_arrow_pressed():
        print("左箭头键被按下")
