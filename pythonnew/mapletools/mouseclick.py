import pyautogui
import keyboard
# 获取鼠标位置的 X 和 Y 坐标
import time

running = False
click=False


def on_key_press(event):
    global running
    if event.name == '0':
        running = not running
        if running:
            print("循环已启动")
        else:
            print("循环已暂停")
    if event.name == '9':
        click = not click
        if click:
            print("点击已启动")
        else:
            print("点击已暂停")
                
print("加载完毕，请按数字 0 启动/暂停")
keyboard.on_press(on_key_press)

while True:
    if running:
        #print(f"当前时间：{datetime.now()} press key :x")
        x, y = pyautogui.position()
        print(f"鼠标位置：X={x}, Y={y}")
    time.sleep(0.5)  
    #if  click:
          
         
     
  
# 打印坐标
 