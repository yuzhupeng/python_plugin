"""用于跟踪游戏中有用信息的模块。"""

import time
import cv2
import threading
import ctypes
import mss
import mss.windows
import numpy as np
from src.common import config, utils
from ctypes import wintypes
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()


# 最小地图顶部与屏幕顶部之间的距离
MINIMAP_TOP_BORDER = 5

# 最小地图的其他三个边界的厚度
MINIMAP_BOTTOM_BORDER = 9

# 用于窗口模式的像素偏移量
WINDOWED_OFFSET_TOP = 36
WINDOWED_OFFSET_LEFT = 10

# 最小地图的左上角和右下角
MM_TL_TEMPLATE = cv2.imread('assets/minimap_tl_template.png', 0)
MM_BR_TEMPLATE = cv2.imread('assets/minimap_br_template.png', 0)

MMT_HEIGHT = max(MM_TL_TEMPLATE.shape[0], MM_BR_TEMPLATE.shape[0])
MMT_WIDTH = max(MM_TL_TEMPLATE.shape[1], MM_BR_TEMPLATE.shape[1])

# 最小地图上的玩家标志
PLAYER_TEMPLATE = cv2.imread('assets/player_template.png', 0)
PT_HEIGHT, PT_WIDTH = PLAYER_TEMPLATE.shape


class Capture:
    """
    一个类，用于跟踪玩家位置和各种游戏事件。它不断更新config模块中关于这些事件的信息。它还会注释和显示弹出窗口中的最小地图。
    """

    def __init__(self):
        """初始化此Capture对象的主线程。"""

        config.capture = self

        self.frame = None
        self.minimap = {}
        self.minimap_ratio = 1
        self.minimap_sample = None
        self.sct = None
        self.window = {
            'left': 0,
            'top': 0,
            'width': 1366,
            'height': 768
        }

        self.ready = False
        self.calibrated = False
        self.thread = threading.Thread(target=self._main)
        self.thread.daemon = True

    def start(self):
        """启动此Capture的线程。"""

        print('\n[~] Started video capture')
        self.thread.start()

    def _main(self):
        """不断监视玩家位置和游戏事件。"""

        mss.windows.CAPTUREBLT = 0
        while True:
            # 校准屏幕截图
            handle = user32.FindWindowW(None, 'MapleStory')
            rect = wintypes.RECT()
            user32.GetWindowRect(handle, ctypes.pointer(rect))
            rect = (rect.left, rect.top, rect.right, rect.bottom)
            rect = tuple(max(0, x) for x in rect)

            self.window['left'] = rect[0]
            self.window['top'] = rect[1]
            self.window['width'] = max(rect[2] - rect[0], MMT_WIDTH)
            self.window['height'] = max(rect[3] - rect[1], MMT_HEIGHT)

            # 通过找到最小地图的左上角和右下角来校准
            with mss.mss() as self.sct:
                self.frame = self.screenshot()
            if self.frame is None:
                continue
            tl, _ = utils.single_match(self.frame, MM_TL_TEMPLATE)
            _, br = utils.single_match(self.frame, MM_BR_TEMPLATE)
            mm_tl = (
                tl[0] + MINIMAP_BOTTOM_BORDER,
                tl[1] + MINIMAP_TOP_BORDER
            )
            mm_br = (
                max(mm_tl[0] + PT_WIDTH, br[0] - MINIMAP_BOTTOM_BORDER),
                max(mm_tl[1] + PT_HEIGHT, br[1] - MINIMAP_BOTTOM_BORDER)
            )
            self.minimap_ratio = (mm_br[0] - mm_tl[0]) / (mm_br[1] - mm_tl[1])
            self.minimap_sample = self.frame[mm_tl[1]
                :mm_br[1], mm_tl[0]:mm_br[0]]
            self.calibrated = True

            with mss.mss() as self.sct:
                while True:
                    if not self.calibrated:
                        break

                    # 截图
                    self.frame = self.screenshot()
                    if self.frame is None:
                        continue

                    # 将帧裁剪为只显示最小地图
                    minimap = self.frame[mm_tl[1]:mm_br[1], mm_tl[0]:mm_br[0]]

                    # 确定玩家位置
                    player = utils.multi_match(
                        minimap, PLAYER_TEMPLATE, threshold=0.8)
                    if player:
                        config.player_pos = utils.convert_to_relative(
                            player[0], minimap)

                    # 打包显示信息以供GUI轮询
                    self.minimap = {
                        'minimap': minimap,
                        'rune_active': config.bot.rune_active,
                        'rune_pos': config.bot.rune_pos,
                        'path': config.path,
                        'player_pos': config.player_pos
                    }

                    if not self.ready:
                        self.ready = True
                    time.sleep(0.001)

    def screenshot(self, delay=1):
        try:
            return np.array(self.sct.grab(self.window))
        except mss.exception.ScreenShotError:
            print(f'\n[!] Error while taking screenshot, retrying in {delay} second'
                  + ('s' if delay != 1 else ''))
            time.sleep(delay)
