import os  # 用于文件操作
import time    #用于记录每一项操作的时间
import json    #用于保存导出我们记录的操作
import threading    #由于键盘和鼠标事件的监听都是阻塞的,所以用两个线程实现
import tkinter  #绘制操作界面
from tkinter import messagebox
from tkinter.ttk import Separator
from postmessage import key_down, key_up
import pynput    #用于记录用户事件
import ctypes
import sys
from ctypes import windll

PROCESS_PER_MONITOR_DPI_AWARE = 2  #解决由于屏幕分辨率缩放导致的，pynput监听鼠标位置不准的问题
ctypes.windll.shcore.SetProcessDpiAwareness(PROCESS_PER_MONITOR_DPI_AWARE)

command_list=[]    #用来存储用户的操作
command_read=[]    #用来读取录制的操作
isRunning=True    #是否在运行,用于实现在按esc后退出的功能
isCon=False
int_time=1000
startTime=0    #开始时间,会在之后main函数中进行初始化
mouse_x_old = 0
mouse_y_old = 0
mouse_t_old = 0

def on_press(key):
    if key == pynput.Key.f1:
        # Stop the execution
        return False
    
if not windll.shell32.IsUserAnAdmin():
        # 不是管理员就提权
        windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, __file__, None, 1)

import cv2
hwnd = windll.user32.FindWindowW(None, "notepad++") 


def on_key_press(key):    #当按键按下时记录
    if key==pynput.keyboard.Key.esc:    #如果是esc
        global isRunning
        isRunning=False    #通知监听鼠标的线程
        mouse=pynput.mouse.Controller()    #获取鼠标的控制器
        mouse.click(pynput.mouse.Button.left)    #通过模拟点击鼠标以执行鼠标的线程,然后退出监听.
        return False    #监听函数return False表示退出监听12
    command_list.append((
        "press",    #操作模式
        (str(key).strip("'"),),    #具体按下的键,传进来的参数并不是一个字符串,而是一个对象,如果按下的是普通的键,会记录下键对应的字符,否则会使一个"Key.xx"的字符串
        time.time()-startTime    #操作距离程序开始运行的秒数
    ))
def on_key_release(key):    #但按键松开时记录
    command_list.append((
        "release",    #操作模式
        (str(key).strip("'"),),    #键信息,参见on_key_press中的相同部分
        time.time()-startTime    #操作距离程序开始运行的秒数
    ))

def on_mouse_click(x,y,button,pressed):
    global mouse_x_old
    global mouse_y_old
    global mouse_t_old
    if not isRunning:    #如果已经不在运行了
        return False    #退出监听
    if not pressed:    #如果是松开事件
        return True    #不记录
    if mouse_x_old == x and mouse_y_old == y:
        if time.time() - mouse_t_old > 0.3: #如果两次点击时间小于0.3秒就会判断为双击 否则就是单击
            command_list.append((
                "click",  # 操作模式
                (x, y, str(button)),  # 分别是鼠标的坐标和按下的按键
                time.time() - startTime  # 操作距离程序开始运行的秒数
            ))
        else:
            command_list.pop(0)  #删除前一个
            command_list.append((
                "double-click",  # 操作模式
                (x, y, str(button)),  # 分别是鼠标的坐标和按下的按键
                time.time() - startTime  # 操作距离程序开始运行的秒数
            ))
    else:
        command_list.append((
            "click",  # 操作模式
            (x, y, str(button)),  # 分别是鼠标的坐标和按下的按键
            time.time() - startTime  # 操作距离程序开始运行的秒数
        ))
    mouse_x_old = x
    mouse_y_old = y
    mouse_t_old = time.time()
def start_key_listen():    #用于开始按键的监听
    # 进行监听
    with pynput.keyboard.Listener(on_press=on_key_press,on_release=on_key_release) as listener:
        listener.join()

def start_mouse_listen():    #用于开始鼠标的监听
    # 进行监听
    with pynput.mouse.Listener(on_click=on_mouse_click) as listener:
        listener.join()

def toFile(command_list,path):    #保存为文件,参数分别为操作记录和保存位置
    with open(path,"w") as f:
        f.write(json.dumps(command_list))    #使用json格式写入

def unicode_convert(input_data):
    #将unicode转换成str
    if isinstance(input_data, dict):
        return {unicode_convert(key): unicode_convert(value) for key, value in input_data.iteritems()}
    elif isinstance(input_data, list):
        return [unicode_convert(element) for element in input_data]
    elif isinstance(input_data, str):
        return input_data
    else:
        return input_data

def ExecuteCommandsFile(path):
    # 如果命令行传入了参数,则使用命令行参数,否则提示用户输入,此变量表示操作记录文件的路径
    # 第二个不是:,也就代表路径是相对路径
    path = unicode_convert(path)
    if path[2] != ":":
        # 将其解析为从本文件开始的路径
        path = os.path.join(os.path.dirname(__file__), path)

    # 打开文件
    with open(path) as f:
        # 将记录的命令写入命令列表
        command_read = json.loads(f.read())
    command_read = unicode_convert(command_read)
    # 创建鼠标和键盘的执行器,用于模拟键盘和鼠标的操作
    mouse = pynput.mouse.Controller()
    keyboard = pynput.keyboard.Controller()
    # 鼠标的两个按钮
    buttons = {
        "Button.left": pynput.mouse.Button.left,
        "Button.right": pynput.mouse.Button.right
    }
    # 开始后已经经过的时间
    sTime = 0
    # 创建一个键盘监听器
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    # 执行每一条记录
    for command in command_read:
        # 如果按下F1键，则停止操作
        if listener.stopped:
            break
        # 如果是点击记录
        print(command[0])
        print(command[1])
        print(command[2])
        # 如果是单击
        if command[0] == "click":
            # 将鼠标移动到记录中的位置
            mouse.position = (command[1][0], command[1][1])
            # 等待一下
            time.sleep(0.1)
            # 点击
            mouse.click(buttons[command[1][2]])
        # 如果是双击
        elif command[0] == "double-click":
            # 将鼠标移动到记录中的位置
            mouse.position = (command[1][0], command[1][1])
            # 等待一下
            time.sleep(0.1)
            # 双击
            mouse.click(buttons[command[1][2]], 2)
        # 如果是按键按下
        elif command[0] == "press":
            # 如果是特殊按键,会记录成Key.xxx,这里判断是不是特殊按键
            if command[1][0][:3] == "Key":
                # 按下按键
                print(command[1][0])
                key_down(hwnd, command[1][0])
                #keyboard.press(eval(command[1][0], {}, {"Key": pynput.keyboard.Key}))
            else:
                # 如果是普通按键,直接按下
                if "<255>" == command[1][0]:
                    continue
                print(command[1][0])
                print(command[1][0])
                key_down(hwnd, command[1][0])
                # print(command[1][0].split("'")[1])
                # keyboard.press(command[1][0].split("'")[1])
                #keyboard.press(command[1][0])
        # 如果是按键释放
        elif command[0] == "release":
            # 如果是特殊按键
            if command[1][0][:3] == "Key":
                # 按下按键
                #keyboard.release(eval(command[1][0], {}, {"Key": pynput.keyboard.Key}))
                print(command[1][0])
                key_up(hwnd, command[1][0])
            else:
                # 普通按键直接按下
                if "<255>" == command[1][0]:
                    continue
             
                print(command[1][0])
                key_up(hwnd, command[1][0])
                # print(command[1][0].split("'")[1])
                # keyboard.release(command[1][0].split("'")[1])
                #keyboard.release(command[1][0])
        # command[2]代表此操作距离开始操作所经过的时间,用它减去已经经过的时间就是距离下一次操作的时间
        time.sleep(command[2] - sTime)
        # 更新时间
        sTime = command[2]
    
    # Stop the keyboard listener
    listener.stop()
class TKDemo:
    def __init__(self):
        self.top = tkinter.Tk()
        self.top.title('鼠标宏录制工具')
        self.top.geometry('500x500')

        frame1 = tkinter.Frame(self.top)
        frame1.pack(side='top')

        l1 = tkinter.Label(frame1,
                           text='【鼠标操作录制功能】\n\n【1：录制操作】\n注意：按Esc退出录制，暂不支持键盘组合键')
        l1.pack()
        b1 = tkinter.Button(frame1,
                            text='录制',
                            width=15, height=2,
                            command=self.recordOp)
        b1.pack()
        frame2 = tkinter.Frame(self.top)
        frame2.pack(after=frame1)
        l2 = tkinter.Label(frame2,
                           text='【2：执行操作】')
        l2.pack()
        l3 = tkinter.Label(frame2,
                           text='请输入执行次数，默认为1次')
        l3.pack()
        self.count = tkinter.StringVar()
        e1= tkinter.Entry(frame2, textvariable=self.count)
        e1.pack()
        b2 = tkinter.Button(frame2,
                            text='执行',
                            width=15, height=2,
                            command=self.execOp)
        b2.pack()

        #分割线
        sep1 = Separator(self.top,orient='horizontal')
        sep1.pack(padx=10,pady=10,fill='x')

        frame3 = tkinter.Frame(self.top)
        frame3.pack(after=sep1)
        l4 = tkinter.Label(frame3,
                           text='【鼠标左键连点功能】\n\n【1：连点间隔(ms)】')
        l4.pack()
        self.interval = tkinter.StringVar()
        e2 = tkinter.Entry(frame3, textvariable=self.interval)
        e2.pack()
        l5 = tkinter.Label(frame3,
                           text='【2：点击开始】\n鼠标放在连点位置，F8键执行连点，F9键退出')
        l5.pack()
        self.b3 = tkinter.Button(frame3,
                            text='开始',
                            width=15, height=2,
                            command=self.conClick)
        self.b3.pack(after=l5,side='left')
        self.w = tkinter.Canvas(frame3, width=50, height=50)
        self.w.pack(after=l5,side='right')
        self.w.create_oval(2,2,50,50,fill='gray', tags=('LED'))

        self.top.mainloop()

    def recordOp(self):
        self.top.iconify()  #窗口隐藏
        global startTime
        startTime = time.time()  # 初始化开始时间
        key_listen_thread = threading.Thread(target=start_key_listen)  # 创建用于监听按键的线程
        mouse_listen_thread = threading.Thread(target=start_mouse_listen)  # 创建用于监听鼠标的线程
        # 运行线程
        key_listen_thread.start()
        mouse_listen_thread.start()
        # 等待线程结束,也就是等待用户按下esc
        key_listen_thread.join()
        mouse_listen_thread.join()
        # 记录成功之后执行下列操作
        toFile(command_list, "./commands.json")# 保存文件

        global isRunning
        isRunning = True  # 初始化记录状态
        command_list.clear()  # 清空列表
        self.top.deiconify()  # 窗口显现
        print("记录成功！")
        tkinter.messagebox.showinfo('提示', '记录成功！')

    def execOp(self):
        self.top.iconify()  # 窗口隐藏
        path = 'commands.json'
        count = self.count.get()
        if count.isdigit():
            for i in range(int(count)):
                ExecuteCommandsFile(path)
            print("执行成功%d次!" % (int(count)))
            tkinter.messagebox.showinfo('提示', "执行完毕！\n共%d次！" % (int(count)))
        elif len(count) == 0:
            ExecuteCommandsFile(path)
            print("执行成功1次!")
            tkinter.messagebox.showinfo('提示', '执行完毕！\n共1次！')
        else:
            print("执行失败！请键入数字")
            tkinter.messagebox.showerror('提示', '执行失败！\n请键入数字！')
        self.top.deiconify()  # 窗口显现

    ##########################################!!!鼠标连点功能!!!##########################################
    def conClick(self):  #鼠标连点
        global int_time
        int_time = self.interval.get()
        if int_time.isdigit():
            int_time = float(int_time)
            print("准备连点，时间间隔 %f 秒" % (int_time / 1000))
        elif len(int_time) == 0:
            int_time = 1000.0
            print("准备连点，时间间隔 %f 秒" % (int_time / 1000))
        else:
            print("执行失败！请键入数字")
            tkinter.messagebox.showerror('提示', '执行失败！\n请键入数字！')
            return
        # 开启新线程，避免GUI卡死
        t = threading.Thread(target=self.new_thread_start)
        # 开启守护线程，这样在GUI意外关闭时线程能正常退出
        t.setDaemon(True)
        t.start()

    def new_thread_start(self):
        key_listen_thread = pynput.keyboard.Listener(on_press=self.on_key_press_con)
        # 运行线程
        key_listen_thread.start()

    def on_key_press_con(self, key):  # 当连点按键按下时记录
        global isCon
        if key == pynput.keyboard.Key.f8:  # 如果是F8，则开始连点
            isCon = True
            self.b3.config(state='disabled')
            self.w.itemconfigure('LED', fill='green')
            self.mouse_click()
        if key == pynput.keyboard.Key.f9:  # 如果是F9，则退出连点
            isCon = False
            self.b3.config(state='normal')
            self.w.itemconfigure('LED', fill='gray')
            self.mouse_click()
            # tkinter.messagebox.showerror('提示', '结束连点！')

    def mouse_click(self):
        key_listener = pynput.keyboard.Listener(on_press=self.on_key_press_con)
        key_listener.start()
        while isCon:
            mouse = pynput.mouse.Controller()  # 获取鼠标的控制器
            mouse.click(pynput.mouse.Button.left)  # 通过模拟点击鼠标以执行鼠标的线程,然后退出监听.
            time.sleep(int_time / 1000)
        key_listener.stop()


def main():    #主函数
    TKDemo()

if __name__=="__main__":
    main()
