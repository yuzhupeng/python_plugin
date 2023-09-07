"""һ�����ڶ��ģ��ĺ�������ļ��ϡ�"""

import math
import queue
import cv2
import threading
import numpy as np
from src.common import config, settings
from random import random

def run_if_enabled(function):
    """
    װ����������ֻ�е�����������ʱ�����еĺ�����
    :param function: Ҫװ�εĺ�����
    :return: װ�κ�ĺ�����
    """
    def helper(*args, **kwargs):
        if config.enabled:
            return function(*args, **kwargs)
        return helper
    return helper

def run_if_disabled(message=''):
    """
    װ����������ֻ�е������˽���ʱ�����еĺ��������MESSAGE��Ϊ�գ������������ڲ�Ӧ����ʱ���������ӡ����Ϣ��
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
    Ӧ�þ��빫ʽ�������㡣
    :param a: ��һ���㡣
    :param b: �ڶ����㡣
    :return: ������֮��ľ��롣
    """
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def separate_args(arguments):
    """
    ������������ARGUMENTS����Ϊһ����ͨ�����������һ���ؼ��ֲ������ֵ䡣
    :param arguments: Ҫ����Ĳ������顣
    :return: һ����ͨ�����������һ���ؼ��ֲ������ֵ䡣
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
    ��FRAME���ҵ����ƥ���
    :param frame: Ҫ����TEMPLATE��ͼ��
    :param template: Ҫƥ���ģ�塣
    :return: ���ƥ��������ϽǺ����½�λ�á�
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)
    _, _, _, top_left = cv2.minMaxLoc(result)
    w, h = template.shape[::-1]
    bottom_right = (top_left[0] + w, top_left[1] + h)
    return top_left, bottom_right

def multi_match(frame, template, threshold=0.95):
    """
    ��FRAME���ҵ�������TEMPLATE���Ƶ�ƥ������ƶ�����ΪTHRESHOLD��
    :param frame: Ҫ������ͼ��
    :param template: Ҫƥ���ģ�塣
    :param threshold: ÿ���������ƥ���TEMPLATE����С�ٷֱȡ�
    :return: ����THRESHOLD��ƥ�������顣
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
    ����FRAME��POINTת��Ϊ������귶ΧΪ[0, 1]��
    ʹ��config.mm_ratioͨ������ֱ��ĵ�λ��׼��Ϊ��ˮƽ����ȵĵ�λ��
    :param point: ���������еĵ㡣
    :param frame: �����ο���ͼ��
    :return: ��������и����ĵ㡣
    """
    x = point[0] / frame.shape[1]
    y = point[1] / config.capture.minimap_ratio / frame.shape[0]
    return x, y

def convert_to_absolute(point, frame):
    """
    ����FRAME��POINTת��Ϊ�������꣨������Ϊ��λ����
    ʹ��config.mm_ratioͨ������ֱ��ĵ�λ��׼��Ϊ��ˮƽ����ȵĵ�λ��
    :param point: ��������еĵ㡣
    :param frame: �����ο���ͼ��
    :return: ������ľ������ꡣ
    """
    x = int(round(point[0] * frame.shape[1]))
    y = int(round(point[1] * config.capture.minimap_ratio * frame.shape[0]))
    return x, y

def filter_color(img, ranges):
    """
    ����һ��ֻ����HSV��Χ�ڵ����صĹ��˸���IMG��
    :param img: Ҫ���˵�ͼ��
    :param ranges: һ��Ԫ���б�ÿ��Ԫ�鶼�����޺�����HSV�Ķԡ�
    :return: IMG�Ĺ��˸�����
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
    ��MINIMAP�ϻ���POINT�Ŀ��ӻ���ʾ��Բ�İ뾶��ʾ��POINT�ƶ�ʱ��������
    :param minimap: Ҫ���Ƶ�ͼ��
    :param pos: Ҫ��ʾ��λ�ã���ΪԪ�飩��
    :param color: Բ����ɫ��
    :return: ��
    """
    center = convert_to_absolute(pos, minimap)
    cv2.circle(minimap,
               center,
               round(minimap.shape[1] * settings.move_tolerance),
               color,
               1)

def print_separator():
    """��ӡ3�������Խ����Ӿ������ȡ�"""
    print('\n\n')

def print_state():
    """��ӡAuto Maple��ǰ�Ƿ����û���á�"""
    print_separator()
    print('#' * 18)
    print(f"#    {'ENABLED ' if config.enabled else 'DISABLED'}    #")
    print('#' * 18)

def closest_point(points, target):
    """
    ����POINTS�о���TARGET����ĵ㡣
    :param points: Ҫ���ĵ��б�
    :param target: Ҫ���ĵ㡣
    :return: ����TARGET����ĵ㣬���POINTSΪ���򷵻�None��
    """
    if points:
        points.sort(key=lambda p: distance(p, target))
        return points[0]

def bernoulli(p):
    """
    ���ظ���ΪP�Ĳ�Ŭ�����������ֵ��
    :param p: �������ΪTrue�ĸ��ʡ�
    :return: True��False��
    """
    return random() < p

def rand_float(start, end):
    """��������[START, END)�е������������"""
    assert start < end, 'START����С��END'
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
