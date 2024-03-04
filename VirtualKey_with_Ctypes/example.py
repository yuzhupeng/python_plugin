from ctypes_key import PressKey, ReleaseKey
from bdtime import vk, tt
import keyboard
import time
# press any ch
def down_up(ch, t = 0.5):
    ch = vk.conv_ord(ch)
    PressKey(ch)
    tt.sleep(t)
    ReleaseKey(ch)
    return 1




running = False

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

         
    

def main():
    # KeyDown and KeyUp
    
    while True:
        if running:
            ch = 'a'
             
            down_up(ch)
            down_up(ch)
            down_up(ch)
            down_up(ch)
            down_up(ch)
            tt.sleep(0.5)
            # select all
            tt.sleep(0.5)
            #down_up(vk.right_arrow)
            #down_up(vk.right_arrow)
            tt.sleep(0.5)
            #down_up(vk.left_arrow)
            #down_up(vk.left_arrow)
            #down_up(vk.left_arrow)
            #down_up(vk.left_arrow)
            #down_up(vk.left_arrow)
            tt.sleep(5)
            PressKey(vk.left_arrow)
            tt.sleep(1)
            ReleaseKey(vk.left_arrow)
            
            PressKey(vk.left_arrow)
            tt.sleep(1)
            ReleaseKey(vk.left_arrow)
            
            PressKey(vk.right_arrow)
            tt.sleep(1)
            ReleaseKey(vk.right_arrow)                        
            PressKey(vk.right_arrow)
            tt.sleep(1)
            ReleaseKey(vk.right_arrow)               
                  
            
    
    
    
     


if __name__ == '__main__':
    main()