"""
一个可以由例程更改的用户定义设置列表。还包含一组验证函数，可用于强制参数类型。
"""

#################################
#      验证函数      #
#################################


def validate_nonnegative_int(value):
    """
    检查VALUE是否为有效的非负整数。
    :param value:   要检查的字符串。
    :return:        VALUE作为整数。
    """
    if int(value) >= 1:
        return int(value)
    raise ValueError(f"'{value}' 不是有效的非负整数。")


def validate_boolean(value):
    """
    检查VALUE是否为有效的Python布尔值。
    :param value:   要检查的字符串。
    :return:        VALUE作为布尔值。
    """
    value = value.lower()
    if value in {'true', 'false'}:
        return True if value == 'true' else False
    elif int(value) in {0, 1}:
        return bool(int(value))
    raise ValueError(f"'{value}' 不是有效的布尔值。")


def validate_arrows(key):
    """
    检查字符串KEY是否为箭头键。
    :param key:     要检查的键。
    :return:        如果KEY是有效的箭头键，则返回小写的KEY。
    """
    if isinstance(key, str):
        key = key.lower()
        if key in ['up', 'down', 'left', 'right']:
            return key
    raise ValueError(f"'{key}' 不是有效的箭头键。")


def validate_horizontal_arrows(key):
    """
    检查字符串KEY是否为左箭头或右箭头键。
    :param key:     要检查的键。
    :return:        如果KEY是有效的水平箭头键，则返回小写的KEY。
    """
    if isinstance(key, str):
        key = key.lower()
        if key in ['left', 'right']:
            return key
    raise ValueError(f"'{key}' 不是有效的水平箭头键。")


#########################
#       设置        #
#########################
# 将每个设置映射到其验证函数的字典
SETTING_VALIDATORS = {
    'move_tolerance': float,
    'adjust_tolerance': float,
    'record_layout': validate_boolean,
    'buff_cooldown': validate_nonnegative_int
}


def reset():
    """将所有设置重置为默认值。"""
    global move_tolerance, adjust_tolerance, record_layout, buff_cooldown
    move_tolerance = 0.1
    adjust_tolerance = 0.01
    record_layout = False
    buff_cooldown = 180


# 移动到目标时允许的误差
move_tolerance = 0.1

# 调整到特定位置时允许的误差
adjust_tolerance = 0.01

# 是否将新的玩家位置保存到当前布局
record_layout = False

# 每次调用'buff'命令之间等待的时间（以秒为单位）
buff_cooldown = 180

reset()
