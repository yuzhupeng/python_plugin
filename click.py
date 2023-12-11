import time
from ctypes import windll
import pyautogui
# 定义常量
HWND = windll.user32.GetForegroundWindow()
WM_MOUSEMOVE = 0x0200
WM_LBUTTONDOWN = 0x0201
WM_LBUTTONUP = 0x202
WM_MOUSEWHEEL = 0x020A



WHEEL_DELTA = 120
def left_down(handle: int, x: int, y: int):
    """在坐标(x, y)按下鼠标左键"""
    wparam = 0
    lparam = y << 16 | x
    windll.user32.PostMessageW(handle, WM_LBUTTONDOWN, wparam, lparam)

def left_up(handle: HWND, x: int, y: int):
    """在坐标(x, y)放开鼠标左键

    Args:
        handle (HWND): 窗口句柄
        x (int): 横坐标
        y (int): 纵坐标
    """
    # https://docs.microsoft.com/en-us/windows/win32/inputdev/wm-lbuttonup
    wparam = 0
    lparam = y << 16 | x
    windll.user32.PostMessageW(handle, WM_LBUTTONUP, wparam, lparam)


def test_left_down():
    #x = 100  # 设置横坐标
    #y = 100  # 设置纵坐标
    num_clicks = 555  # 设置按下次数
    x, y = pyautogui.position()
    print(f"鼠标位置：X={x}, Y={y}")
    for _ in range(num_clicks):
        left_down(HWND, x, y)
        left_down(HWND, x, y)
        left_down(HWND, x, y)
        left_up(HWND, x, y)
        time.sleep(0.3)  # 添加延迟，等待1秒钟
        d, s = pyautogui.position()
        print(f"鼠标位置：X={d}, Y={s}")

# 调用测试函数
test_left_down()