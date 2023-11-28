from ctypes import windll
from ctypes.wintypes import HWND
import string
import time
import tkinter as tk
import keyboard

PostMessageW = windll.user32.PostMessageW
MapVirtualKeyW = windll.user32.MapVirtualKeyW
VkKeyScanA = windll.user32.VkKeyScanA

WM_KEYDOWN = 0x100
WM_KEYUP = 0x101

# https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes
VkCode = {
    "back":  0x08,
    "tab":  0x09,
    "return":  0x0D,
    "shift":  0x10,
    "control":  0x11,
    "menu":  0x12,
    "pause":  0x13,
    "capital":  0x14,
    "escape":  0x1B,
    "space":  0x20,
    "end":  0x23,
    "home":  0x24,
    "left":  0x25,
    "up":  0x26,
    "right":  0x27,
    "down":  0x28,
    "print":  0x2A,
    "snapshot":  0x2C,
    "insert":  0x2D,
    "delete":  0x2E,
    "lwin":  0x5B,
    "rwin":  0x5C,
    "numpad0":  0x60,
    "numpad1":  0x61,
    "numpad2":  0x62,
    "numpad3":  0x63,
    "numpad4":  0x64,
    "numpad5":  0x65,
    "numpad6":  0x66,
    "numpad7":  0x67,
    "numpad8":  0x68,
    "numpad9":  0x69,
    "multiply":  0x6A,
    "add":  0x6B,
    "separator":  0x6C,
    "subtract":  0x6D,
    "decimal":  0x6E,
    "divide":  0x6F,
    "f1":  0x70,
    "f2":  0x71,
    "f3":  0x72,
    "f4":  0x73,
    "f5":  0x74,
    "f6":  0x75,
    "f7":  0x76,
    "f8":  0x77,
    "f9":  0x78,
    "f10":  0x79,
    "f11":  0x7A,
    "f12":  0x7B,
    "numlock":  0x90,
    "scroll":  0x91,
    "lshift":  0xA0,
    "rshift":  0xA1,
    "lcontrol":  0xA2,
    "rcontrol":  0xA3,
    "lmenu":  0xA4,
    "rmenu":  0XA5
}


def get_virtual_keycode(key: str):
    """根据按键名获取虚拟按键码

    Args:
        key (str): 按键名

    Returns:
        int: 虚拟按键码
    """
    if len(key) == 1 and key in string.printable:
        # https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-vkkeyscana
        return VkKeyScanA(ord(key)) & 0xff
    else:
        return VkCode[key]


def key_down(handle: HWND, key: str):
    """按下指定按键

    Args:
        handle (HWND): 窗口句柄
        key (str): 按键名
    """
    vk_code = get_virtual_keycode(key)
    scan_code = MapVirtualKeyW(vk_code, 0)
    # https://docs.microsoft.com/en-us/windows/win32/inputdev/wm-keydown
    wparam = vk_code
    lparam = (scan_code << 16) | 1
    PostMessageW(handle, WM_KEYDOWN, wparam, lparam)


def key_up(handle: HWND, key: str):
    """放开指定按键

    Args:
        handle (HWND): 窗口句柄
        key (str): 按键名
    """
    vk_code = get_virtual_keycode(key)
    scan_code = MapVirtualKeyW(vk_code, 0)
    # https://docs.microsoft.com/en-us/windows/win32/inputdev/wm-keyup
    wparam = vk_code
    lparam = (scan_code << 16) | 0XC0000001
    PostMessageW(handle, WM_KEYUP, wparam, lparam)


if __name__ == "__main__":
    # 需要和目标窗口同一权限，游戏窗口通常是管理员权限
    import sys
    if not windll.shell32.IsUserAnAdmin():
        # 不是管理员就提权
        windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, __file__, None, 1)

    import cv2
    handle = windll.user32.FindWindowW(None, "MapleStory")
    # 控制角色向前移动两秒
 
 
 
 # 处理按键按钮点击事件的函数
def handle_button_click(key):
    interval = float(interval_entry.get())
    enable = enable_var.get()

    if enable:
        for _ in range(10):
            key_down(key)
            key_down(handle, key)
            time.sleep(interval)
            key_up(handle,key)

# 启动/停止所有按键操作
def handle_start_stop():
    global running
    running = not running
    if running:
        start_stop_button.config(text="停止")
        for button in buttons:
            button.config(state=tk.DISABLED)
        start_keys()
    else:
        start_stop_button.config(text="启动")
        for button in buttons:
            button.config(state=tk.NORMAL)

# 启动所有按键操作
def start_keys():
    for key in button_keys:
        interval = float(key_intervals[key].get())
        if enable_var.get():
            for _ in range(10):
                key_down(key)
                time.sleep(interval)
                key_up(key)

# 创建GUI
root = tk.Tk()
root.title("按键操作")

button_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
buttons = []
key_intervals = {}

# 添加按键按钮和对应的时间间隔输入框
for key in button_keys:
    key_frame = tk.Frame(root)
    key_frame.pack()
    
    button = tk.Button(key_frame, text=key, width=10, height=5, command=lambda k=key: handle_button_click(k))
    button.pack(side=tk.LEFT)
    buttons.append(button)
    
    interval_label = tk.Label(key_frame, text="时间间隔:")
    interval_label.pack(side=tk.LEFT)
    
    interval_entry = tk.Entry(key_frame)
    interval_entry.pack(side=tk.LEFT)
    key_intervals[key] = interval_entry

# 添加启动/停止按钮
start_stop_button = tk.Button(root, text="启动", command=handle_start_stop)
start_stop_button.pack()

# 添加启用/禁用复选框
enable_var = tk.BooleanVar()
enable_checkbox = tk.Checkbutton(root, text="启用按键", variable=enable_var)
enable_checkbox.pack()

# 运行GUI
running = False
root.mainloop()
 
 
 
 
 
 
 
 
 
 
 
'''  
running = False

def on_key_press(event):
    global running
    if event.name == '0':
        running = not running
        if running:
            print("循环已启动")
        else:
            print("循环已暂停")

keyboard.on_press(on_key_press)

while True:
    if running:
        key_down(handle, 'x')
        key_up(handle,'x')  
        if time.time() % 11 == 0:
          time.sleep(1)
          key_down(handle, 'a')
          key_up(handle, 'a')
          time.sleep(0.5)
          key_down(handle, 'e')
          key_up(handle, 'e')
        if time.time() % 60 == 0:
          time.sleep(1)
          key_down(handle, 'e')
          key_up(handle, 'e')  
    time.sleep(0.1)    
      '''
  