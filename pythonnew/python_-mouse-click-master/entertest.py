import ctypes
import time
# 定义常量
WM_KEYDOWN = 0x0100
VK_RETURN = 0x0D


def send_enter_to_notepad_pp():
    # 获取Notepad++窗口句柄
    notepad_pp_handle = ctypes.windll.user32.FindWindowW(None, "Notepad++")

    if notepad_pp_handle != 0:
        # 向Notepad++发送Enter键消息
        ctypes.windll.user32.PostMessageW(
            notepad_pp_handle, WM_KEYDOWN, VK_RETURN, 0)


running = True
if __name__ == "__main__":
   while True:
     if running:
        # print(f"当前时间：{datetime.now()} press key :x")
       send_enter_to_notepad_pp()
       time.sleep(0.5)
