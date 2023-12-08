from ctypes import windll, byref
from ctypes.wintypes import HWND, POINT

# 定义 Windows API 函数和常量
user32 = ctypes.windll.user32
GetCursorPos = user32.GetCursorPos
GetCursorPos.argtypes = [wintypes.POINT]
PostMessageW = user32.PostMessageW
WM_LBUTTONDOWN = 0x0201

def left_down(handle: wintypes.HWND, x: int, y: int):
    """在坐标(x, y)按下鼠标左键

    Args:
        handle (wintypes.HWND): 窗口句柄
        x (int): 横坐标
        y (int): 纵坐标
    """
    wparam = 0
    lparam = y << 16 | x
    PostMessageW(handle, WM_LBUTTONDOWN, wparam, lparam)



if __name__ == "__main__":
    # 需要和目标窗口同一权限，游戏窗口通常是管理员权限
    import sys
    if not windll.shell32.IsUserAnAdmin():
        # 不是管理员就提权
        windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, __file__, None, 1)

 
    

handle = windll.user32.FindWindowW(None, "notepad++")



# 获取当前鼠标位置
point = wintypes.POINT()
GetCursorPos(ctypes.byref(point))
x = point.x
y = point.y
print(f"鼠标位置：X={x}, Y={y}")

# 调用 left_down 函数点击当前位置
for i in range(0, 20, 1):
 left_down(handle, x, y)