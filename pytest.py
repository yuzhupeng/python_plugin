import win32api
import win32gui
import pythoncom
import pyHook
import time
from tkinter import Tk, Button

def on_keyboard_event(event):
    global actions
    
    # 记录按下的键
    if event.MessageName == 'key down':
        actions.append(event.Key)
    
    # 检查是否停止录制
    if event.Key == 'Escape':
        return False
    
    return True

def record_keyboard_actions(hwnd):
    global actions
    
    actions = []
    
    # 创建键盘钩子
    hook_manager = pyHook.HookManager()
    hook_manager.KeyDown = on_keyboard_event
    
    # 启动键盘钩子
    hook_manager.HookKeyboard()
    
    # 进入消息循环
    pythoncom.PumpMessages()
    
    return actions

def replay_keyboard_actions(hwnd, actions):
    # 激活窗口
    win32gui.SetForegroundWindow(hwnd)
    
    # 模拟键盘操作
    for key in actions:
        # 按下键
        win32api.keybd_event(ord(key), 0, 0, 0)
        
        # 等待一小段时间
        time.sleep(0.1)
        
        # 释放键
        win32api.keybd_event(ord(key), 0, win32api.KEYEVENTF_KEYUP, 0)

def start_recording(hwnd):
    global recording, actions
    
    if not recording:
        actions = record_keyboard_actions(hwnd)
        recording = True

def stop_recording():
    global recording
    
    recording = False

def replay_actions(hwnd):
    global actions
    
    replay_keyboard_actions(hwnd, actions)

# 获取目标应用程序窗口句柄
app_title = "目标应用程序标题"
hwnd = win32gui.FindWindow(None, app_title)

if hwnd != 0:
    # 创建UI界面
    root = Tk()
    
    # 创建按钮
    start_button = Button(root, text="开始录制", command=lambda: start_recording(hwnd))
    start_button.pack()
    
    stop_button = Button(root, text="停止录制", command=stop_recording)
    stop_button.pack()
    
    replay_button = Button(root, text="回放操作", command=lambda: replay_actions(hwnd))
    replay_button.pack()
    
    # 启动UI界面
    root.mainloop()
    
else:
    print("找不到目标应用程序窗口")