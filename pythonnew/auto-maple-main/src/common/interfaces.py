"""A collection of variables shared across multiple modules."""  # 一个在多个模块之间共享的变量集合

#########################
#       Constants       #
#########################
RESOURCES_DIR = 'resources'  # 资源目录


#################################
#       Global Variables        #
#################################
# The player's position relative to the minimap
player_pos = (0, 0)  # 玩家相对于小地图的位置

# Describes whether the main bot loop is currently running or not
enabled = False  # 描述主要机器人循环当前是否正在运行

# If there is another player in the map, Auto Maple will purposely make random human-like mistakes
stage_fright = False  # 如果地图中有另一个玩家，Auto Maple将故意犯一些随机的类人错误

# Represents the current shortest path that the bot is taking
path = []  # 表示机器人当前正在采取的最短路径


#############################
#       Shared Modules      #
#############################
# A Routine object that manages the 'machine code' of the current routine
routine = None  # 一个管理当前例程的“机器码”的Routine对象

# Stores the Layout object associated with the current routine
layout = None  # 存储与当前例程关联的Layout对象

# Shares the main bot loop
bot = None  # 共享主要机器人循环

# Shares the video capture loop
capture = None  # 共享视频捕获循环

# Shares the keyboard listener
listener = None  # 共享键盘监听器

# Shares the gui to all modules
gui = None  # 共享GUI给所有模块
