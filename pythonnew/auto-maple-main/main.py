import time  # 导入time模块，用于添加延时

from src.modules.bot import Bot  # 从src.modules.bot模块导入Bot类
from src.modules.capture import Capture  # 从src.modules.capture模块导入Capture类
from src.modules.notifier import Notifier  # 从src.modules.notifier模块导入Notifier类
from src.modules.listener import Listener  # 从src.modules.listener模块导入Listener类
from src.modules.gui import GUI  # 从src.modules.gui模块导入GUI类

bot = Bot()  # 创建Bot对象
capture = Capture()  # 创建Capture对象
notifier = Notifier()  # 创建Notifier对象
listener = Listener()  # 创建Listener对象

bot.start()  # 启动Bot模块
while not bot.ready:  # 循环等待Bot模块就绪
    time.sleep(0.01)  # 延时0.01秒

capture.start()  # 启动Capture模块
while not capture.ready:  # 循环等待Capture模块就绪
    time.sleep(0.01)  # 延时0.01秒

notifier.start()  # 启动Notifier模块
while not notifier.ready:  # 循环等待Notifier模块就绪
    time.sleep(0.01)  # 延时0.01秒

listener.start()  # 启动Listener模块
while not listener.ready:  # 循环等待Listener模块就绪
    time.sleep(0.01)  # 延时0.01秒

print('\n[~] Successfully initialized Auto Maple')  # 打印初始化成功的提示信息

gui = GUI()  # 创建GUI对象
gui.start()  # 启动GUI模块
