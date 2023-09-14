from ctypes import windll
from ctypes.wintypes import HWND
import string
import time
from input import presss, key_downs, key_ups


PostMessageW = windll.user32.PostMessageW
MapVirtualKeyW = windll.user32.MapVirtualKeyW
VkKeyScanA = windll.user32.VkKeyScanA

WM_KEYDOWN = 0x100
WM_KEYUP = 0x101

# https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes
 
VkCode = {
    'left': 0x25,   # Arrow keys
    'up': 0x26,
    'right': 0x27,
    'down': 0x28,

    'backspace': 0x08,      # Special keys
    'tab': 0x09,
    'enter': 0x0D,
    'shift': 0x10,
    'ctrl': 0x11,
    'alt': 0x12,
    'caps lock': 0x14,
    'esc': 0x1B,
    'space': 0x20,
    'page up': 0x21,
    'page down': 0x22,
    'end': 0x23,
    'home': 0x24,
    'insert': 0x2D,
    'delete': 0x2E,

    '0': 0x30,      # Numbers
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    '5': 0x35,
    '6': 0x36,
    '7': 0x37,
    '8': 0x38,
    '9': 0x39,

    'a': 0x41,      # Letters
    'b': 0x42,
    'c': 0x43,
    'd': 0x44,
    'e': 0x45,
    'f': 0x46,
    'g': 0x47,
    'h': 0x48,
    'i': 0x49,
    'j': 0x4A,
    'k': 0x4B,
    'l': 0x4C,
    'm': 0x4D,
    'n': 0x4E,
    'o': 0x4F,
    'p': 0x50,
    'q': 0x51,
    'r': 0x52,
    's': 0x53,
    't': 0x54,
    'u': 0x55,
    'v': 0x56,
    'w': 0x57,
    'x': 0x58,
    'y': 0x59,
    'z': 0x5A,

    'f1': 0x70,     # Functional keys
    'f2': 0x71,
    'f3': 0x72,
    'f4': 0x73,
    'f5': 0x74,
    'f6': 0x75,
    'f7': 0x76,
    'f8': 0x77,
    'f9': 0x78,
    'f10': 0x79,
    'f11': 0x7A,
    'f12': 0x7B,
    'num lock': 0x90,
    'scroll lock': 0x91,

    ';': 0xBA,      # Special characters
    '=': 0xBB,
    ',': 0xBC,
    '-': 0xBD,
    '.': 0xBE,
    '/': 0xBF,
    '`': 0xC0,
    '[': 0xDB,
    '\\': 0xDC,
    ']': 0xDD,
    "'": 0xDE
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
    # 需要和目标窗口同一权限，窗口通常是管理员权限
    import sys
    if not windll.shell32.IsUserAnAdmin():
        # 不是管理员就提权
        windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, __file__, None, 1)

    import cv2
    handle = windll.user32.FindWindowW(None, "notepad")
 
 
    time.sleep(5)
    print(1)
    key_downs('left')
    
    key_down(handle, 'w')
    time.sleep(2)
    key_up(handle, 'w')
    
    key_downs('right')
    
    key_downs('left')
    
    key_down(handle, 'w')
    time.sleep(2)
    key_up(handle, 'w')
    
    key_downs('right')
    print(2)