from encodings import utf_8
from time import sleep
# from matplotlib.pyplot import title
import win32gui, win32ui, win32con, win32api
import win32process
import keyboard
import clipboard
from src.common.vkeys import key_down, key_up, press
from pynput.keyboard import Key, Controller
from ctypes import windll
sleep(2)
# clipboard.copy("火焰精靈")  # now the clipboard content will be string "abc"
# keyboard = Controller()
# # # with keyboard.pressed(Key.ctrl_l):
# # #     keyboard.press('v')
# # #     keyboard.release('v')
# # # press("c")
# # print(Key.shift.value)

# print(Key['shift'])
# keyboard.press('shift')
# keyboard.release('shift')
# keyboard.type("cji3u04ru/ xu/6")

# key_down("ctrl")
# key_down('v')
# sleep(0.3)
# key_up('v')
# key_up("ctrl")
# msg = u'火焰精靈'
# encoded = msg.encode('Big5')
# print(encoded)
# msg = encoded.decode('utf_8')
# keyboard.write(encoded)
# window_name = "MapleStory"
# hwnd = win32gui.FindWindow(None, window_name)
# win32gui.SetForegroundWindow(hwnd)
# win32api.PostMessage(hwnd, win32con.WM_PASTE, 1, 11)
# exit()
def list_window_names():
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            print(hex(hwnd), '"' + win32gui.GetWindowText(hwnd) + '"')
    win32gui.EnumWindows(winEnumHandler, None)

list_window_names()

# window_name = "MapleStory"
# hwnd = win32gui.FindWindow(None, window_name)
# # win = win32ui.CreateWindowFromHandle(hwnd)
# # win32gui.SetForegroundWindow(hwnd)
# # # remote_thread, _ = win32process.GetWindowThreadProcessId(hwnd)
# # # win32process.AttachThreadInput(win32api.GetCurrentThreadId(), remote_thread, True)
# # # prev_handle = win32gui.SetFocus(hwnd)
# # # win32gui.SetFocus(hwnd)
# # # sleep(0.5)
# # win.SendMessage(win32con.WM_CHAR, ord('A'), 0)
# # # # #win.SendMessage(win32con.WM_CHAR, ord('B'), 0)
# # # # win.SendMessage(win32con.WM_KEYDOWN, 0x41, 0x001E0001)
# # # # sleep(0.5)
# # win32api.SendMessage(win32con.WM_KEYUP, 0x41, 0xC01E0001)
# # # # sleep(50)
# msg = "123火"
# for i in msg:
#     windll.user32.PostMessageW(hwnd, win32con.WM_CHAR, ord(i), 0)
#     sleep(0.2)
#     # win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x41, 0)
#     sleep(0.3)

# import autoit

# autoit.control_send("[CLASS:MapleStoryClassTW]", None, "{LEFT}")
# autoit.win_close("[CLASS:Notepad]")
# autoit.control_click("[Class:#32770]", "Button2")

# from pywinauto.application import Application

# target_window = win32gui.FindWindow(None, 'MapleStory')
# win32gui.SetForegroundWindow(target_window)
# app = Application(backend="uia")
# app.type (handle=target_window)
# app.send_keys("{a}")
# sleep(2)