"""一个用于多个模块的函数和类的集合。"""

import math
import queue
import cv2
import threading
import numpy as np
from src.common import config, settings
from random import random

def run_if_enabled(function):
    """
    装饰器，用于只有当机器人启用时才运行的函数。
    :param function: 要装饰的函数。
    :return: 装饰后的函数。
    """
    def helper(*args, **kwargs):
        if config.enabled:
            return function(*args, **kwargs)
        return helper
    return helper

def run_if_disabled(message=''):
    """
    装饰器，用于只有当机器人禁用时才运行的函数。如果MESSAGE不为空，当函数尝试在不应运行时，它还会打印该消息。
    """
    def decorator(function):
        def helper(*args, **kwargs):
            if not config.enabled:
                return function(*args, **kwargs)
            elif message:
                print(message)
        return helper
    return decorator

def distance(a, b):
    """
    应用距离公式到两个点。
    :param a: 第一个点。
    :param b: 第二个点。
    :return: 两个点之间的距离。
    """
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def separate_args(arguments):
    """
    将给定的数组ARGUMENTS分离为一个普通参数的数组和一个关键字参数的字典。
    :param arguments: 要分离的参数数组。
    :return: 一个普通参数的数组和一个关键字参数的字典。
    """
    args = []
    kwargs = {}
    for a in arguments:
        a = a.strip()
        index = a.find('=')
        if index > -1:
            key = a[:index].strip()
            value = a[index+1:].strip()
            kwargs[key] = value
        else:
            args.append(a)
    return args, kwargs

def single_match(frame, template):
    """
    在FRAME中找到最佳匹配项。
    :param frame: 要搜索TEMPLATE的图像。
    :param template: 要匹配的模板。
    :return: 最佳匹配项的左上角和右下角位置。
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)
    _, _, _, top_left = cv2.minMaxLoc(result)
    w, h = template.shape[::-1]
    bottom_right = (top_left[0] + w, top_left[1] + h)
    return top_left, bottom_right

def multi_match(frame, template, threshold=0.95):
    """
    在FRAME中找到所有与TEMPLATE相似的匹配项，相似度至少为THRESHOLD。
    :param frame: 要搜索的图像。
    :param template: 要匹配的模板。
    :param threshold: 每个结果必须匹配的TEMPLATE的最小百分比。
    :return: 超过THRESHOLD的匹配项数组。
    """
    if template.shape[0] > frame.shape[0] or template.shape[1] > frame.shape[1]:
        return []
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))
    results = []
    for p in locations:
        x = int(round(p[0] + template.shape[1] / 2))
        y = int(round(p[1] + template.shape[0] / 2))
        results.append((x, y))
    return results

def convert_to_relative(point, frame):
    """
    基于FRAME将POINT转换为相对坐标范围为[0, 1]。
    使用config.mm_ratio通过将垂直轴的单位标准化为与水平轴相等的单位。
    :param point: 绝对坐标中的点。
    :param frame: 用作参考的图像。
    :return: 相对坐标中给定的点。
    """
    x = point[0] / frame.shape[1]
    y = point[1] / config.capture.minimap_ratio / frame.shape[0]
    return x, y

def convert_to_absolute(point, frame):
    """
    基于FRAME将POINT转换为绝对坐标（以像素为单位）。
    使用config.mm_ratio通过将垂直轴的单位标准化为与水平轴相等的单位。
    :param point: 相对坐标中的点。
    :param frame: 用作参考的图像。
    :return: 给定点的绝对坐标。
    """
    x = int(round(point[0] * frame.shape[1]))
    y = int(round(point[1] * config.capture.minimap_ratio * frame.shape[0]))
    return x, y

def filter_color(img, ranges):
    """
    返回一个只包含HSV范围内的像素的过滤副本IMG。
    :param img: 要过滤的图像。
    :param ranges: 一个元组列表，每个元组都是上限和下限HSV的对。
    :return: IMG的过滤副本。
    """
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, ranges[0][0], ranges[0][1])
    for i in range(1, len(ranges)):
        mask = cv2.bitwise_or(mask, cv2.inRange(hsv, ranges[i][0], ranges[i][1]))

    # Mask the image
    color_mask = mask > 0
    result = np.zeros_like(img, np.uint8)
    result[color_mask] = img[color_mask]
    return result

def draw_location(minimap, pos, color):
    """
    在MINIMAP上绘制POINT的可视化表示。圆的半径表示向POINT移动时的允许误差。
    :param minimap: 要绘制的图像。
    :param pos: 要表示的位置（作为元组）。
    :param color: 圆的颜色。
    :return: 无
    """
    center = convert_to_absolute(pos, minimap)
    cv2.circle(minimap,
               center,
               round(minimap.shape[1] * settings.move_tolerance),
               color,
               1)

def print_separator():
    """打印3个空行以进行视觉清晰度。"""
    print('\n\n')

def print_state():
    """打印Auto Maple当前是否启用或禁用。"""
    print_separator()
    print('#' * 18)
    print(f"#    {'ENABLED ' if config.enabled else 'DISABLED'}    #")
    print('#' * 18)

def closest_point(points, target):
    """
    返回POINTS中距离TARGET最近的点。
    :param points: 要检查的点列表。
    :param target: 要检查的点。
    :return: 距离TARGET最近的点，如果POINTS为空则返回None。
    """
    if points:
        points.sort(key=lambda p: distance(p, target))
        return points[0]

def bernoulli(p):
    """
    返回概率为P的伯努利随机变量的值。
    :param p: 随机变量为True的概率。
    :return: True或False。
    """
    return random() < p

def rand_float(start, end):
    """返回区间[START, END)中的随机浮点数。"""
    assert start < end, 'START必须小于END'
    return (end - start) * random() + start

##########################
#       Threading        #
##########################

class Async(threading.Thread):
    def __init__(self, function, *args, **kwargs):
        super().__init__()
        self.queue = queue.Queue()
        self.function = function
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.function(*self.args, **self.kwargs)
        self.queue.put('x')

    def process_queue(self, root):
        def f():
            try:
                self.queue.get_nowait()
            except queue.Empty:
                root.after(100, self.process_queue(root))
        return f


def async_callback(context, function, *args, **kwargs):
    """Returns a callback function that can be run asynchronously by the GUI."""

    def f():
        task = Async(function, *args, **kwargs)
        task.start()
        context.after(100, task.process_queue(context))
    return f
