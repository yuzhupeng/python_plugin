import time
import pyautogui
import keyboard
running=False 
 
def on_key_press(event):
    global running
    if event.name == '0':
        running = not running
        if running:
            print("循环已启动")
        else:
            print("循环已暂停")
print("加载完毕，请按数字 0 启动/暂停")
keyboard.on_press(on_key_press)     
 
 
def test_left_down():
    #x = 100  # 设置横坐标
    #y = 100  # 设置纵坐标
    num_clicks = 555  # 设置按下次数
    x, y = pyautogui.position()
    while True:
     if running:    
        print(f"鼠标位置：X={x}, Y={y}")
        for _ in range(num_clicks):
            if running:
                        x, y = pyautogui.position()
                        pyautogui.click(x, y)
                        pyautogui.click(x, y)
                        pyautogui.click(x, y)
                        pyautogui.click(x, y)
                        pyautogui.press('enter')
                        pyautogui.press('enter')
                        time.sleep(0.3)  # 添加延迟，等待1秒钟
                        d, s = pyautogui.position()
                        print(f"鼠标位置：X={d}, Y={s}")

# 调用测试函数
test_left_down()




 