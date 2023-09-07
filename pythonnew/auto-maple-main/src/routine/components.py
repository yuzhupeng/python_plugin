"""用于执行例行程序的类集合。"""

import math
import time
from src.common import config, settings, utils
from src.common.vkeys import key_down, key_up, press


#################################
#       例行程序组件      #
#################################
class Component:
    id = '例行程序组件'
    PRIMITIVES = {int, str, bool, float}

    def __init__(self, *args, **kwargs):
        if len(args) > 1:
            raise TypeError('Component超类__init__只接受1个（可选）参数：LOCALS')
        if len(kwargs) != 0:
            raise TypeError('Component超类__init__不接受任何关键字参数')
        if len(args) == 0:
            self.kwargs = {}
        elif type(args[0]) != dict:
            raise TypeError("Component超类__init__只接受'type'为'dict'的参数。")
        else:
            self.kwargs = args[0].copy()
            self.kwargs.pop('__class__')
            self.kwargs.pop('self')

    @utils.run_if_enabled
    def execute(self):
        self.main()

    def main(self):
        pass

    def update(self, *args, **kwargs):
        """使用新参数更新此组件的构造函数参数。"""

        self.__class__(*args, **kwargs)     # 在实际更新值之前验证参数
        self.__init__(*args, **kwargs)

    def info(self):
        """返回有关此组件的有用信息的字典。"""

        return {
            '名称': self.__class__.__name__,
            '变量': self.kwargs.copy()
        }

    def encode(self):
        """使用其ID和__init__参数对对象进行编码。"""

        arr = [self.id]
        for key, value in self.kwargs.items():
            if key != 'id' and type(self.kwargs[key]) in Component.PRIMITIVES:
                arr.append(f'{key}={value}')
        return ', '.join(arr)


class Point(Component):
    """表示用户定义例行程序中的位置。"""

    id = '*'

    def __init__(self, x, y, frequency=1, skip='False', adjust='False'):
        super().__init__(locals())
        self.x = float(x)
        self.y = float(y)
        self.location = (self.x, self.y)
        self.frequency = settings.validate_nonnegative_int(frequency)
        self.counter = int(settings.validate_boolean(skip))
        self.adjust = settings.validate_boolean(adjust)
        if not hasattr(self, 'commands'):       # 更新Point不应清除命令
            self.commands = []

    def main(self):
        """执行与此Point关联的一组动作。"""

        if self.counter == 0:
            move = config.bot.command_book['move']
            move(*self.location).execute()
            if self.adjust:
                # TODO: 使用step('up')调整？
                adjust = config.bot.command_book['adjust']
                adjust(*self.location).execute()
            for command in self.commands:
                command.execute()
        self._increment_counter()

    @utils.run_if_enabled
    def _increment_counter(self):
        """增加此Point的计数器，当上限时回到0。"""

        self.counter = (self.counter + 1) % self.frequency

    def info(self):
        curr = super().info()
        curr['变量'].pop('location', None)
        curr['变量']['commands'] = ', '.join([c.id for c in self.commands])
        return curr

    def __str__(self):
        return f'  * {self.location}'


class Label(Component):
    id = '@'

    def __init__(self, label):
        super().__init__(locals())
        self.label = str(label)
        if self.label in config.routine.labels:
            raise ValueError
        self.links = set()
        self.index = None

    def set_index(self, i):
        self.index = i

    def encode(self):
        return '\n' + super().encode()

    def info(self):
        curr = super().info()
        curr['变量']['index'] = self.index
        return curr

    def __delete__(self, instance):
        del self.links
        config.routine.labels.pop(self.label)

    def __str__(self):
        return f'{self.label}:'


class Jump(Component):
    """跳转到给定的Label。"""

    id = '>'

    def __init__(self, label, frequency=1, skip='False'):
        super().__init__(locals())
        self.label = str(label)
        self.frequency = settings.validate_nonnegative_int(frequency)
        self.counter = int(settings.validate_boolean(skip))
        self.link = None

    def main(self):
        if self.link is None:
            print(f"\n[!] 标签 '{self.label}' 不存在。")
        else:
            if self.counter == 0:
                config.routine.index = self.link.index
            self._increment_counter()

    @utils.run_if_enabled
    def _increment_counter(self):
        self.counter = (self.counter + 1) % self.frequency

    def bind(self):
        """
        将此Goto绑定到其对应的Label。如果Label的索引更改，此Goto实例将自动能够访问更新后的值。
        :return:    绑定是否成功
        """

        if self.label in config.routine.labels:
            self.link = config.routine.labels[self.label]
            self.link.links.add(self)
            return True
        return False

    def __delete__(self, instance):
        if self.link is not None:
            self.link.links.remove(self)

    def __str__(self):
        return f'  > {self.label}'


class Setting(Component):
    """更改给定设置变量的值。"""

    id = '$'

    def __init__(self, target, value):
        super().__init__(locals())
        self.key = str(target)
        if self.key not in settings.SETTING_VALIDATORS:
            raise ValueError(f"设置 '{target}' 不存在")
        self.value = settings.SETTING_VALIDATORS[self.key](value)

    def main(self):
        setattr(settings, self.key, self.value)

    def __str__(self):
        return f'  $ {self.key} = {self.value}'


SYMBOLS = {
    '*': Point,
    '@': Label,
    '>': Jump,
    '$': Setting
}


#############################
#       Shared Commands     #
#############################
class Command(Component):
    id = 'Command Superclass'

    def __init__(self, *args):
        super().__init__(*args)
        self.id = self.__class__.__name__

    def __str__(self):
        variables = self.__dict__
        result = '    ' + self.id
        if len(variables) - 1 > 0:
            result += ':'
        for key, value in variables.items():
            if key != 'id':
                result += f'\n        {key}={value}'
        return result


class Move(Command):
    """Moves to a given position using the shortest path based on the current Layout."""

    def __init__(self, x, y, max_steps=15):
        super().__init__(locals())
        self.target = (float(x), float(y))
        self.max_steps = settings.validate_nonnegative_int(max_steps)
        self.prev_direction = ''

    def _new_direction(self, new):
        key_down(new)
        if self.prev_direction and self.prev_direction != new:
            key_up(self.prev_direction)
        self.prev_direction = new

    def main(self):
        counter = self.max_steps
        path = config.layout.shortest_path(config.player_pos, self.target)
        for i, point in enumerate(path):
            toggle = True
            self.prev_direction = ''
            local_error = utils.distance(config.player_pos, point)
            global_error = utils.distance(config.player_pos, self.target)
            while config.enabled and counter > 0 and \
                    local_error > settings.move_tolerance and \
                    global_error > settings.move_tolerance:
                if toggle:
                    d_x = point[0] - config.player_pos[0]
                    if abs(d_x) > settings.move_tolerance / math.sqrt(2):
                        if d_x < 0:
                            key = 'left'
                        else:
                            key = 'right'
                        self._new_direction(key)
                        step(key, point)
                        if settings.record_layout:
                            config.layout.add(*config.player_pos)
                        counter -= 1
                        if i < len(path) - 1:
                            time.sleep(0.15)
                else:
                    d_y = point[1] - config.player_pos[1]
                    if abs(d_y) > settings.move_tolerance / math.sqrt(2):
                        if d_y < 0:
                            key = 'up'
                        else:
                            key = 'down'
                        self._new_direction(key)
                        step(key, point)
                        if settings.record_layout:
                            config.layout.add(*config.player_pos)
                        counter -= 1
                        if i < len(path) - 1:
                            time.sleep(0.05)
                local_error = utils.distance(config.player_pos, point)
                global_error = utils.distance(config.player_pos, self.target)
                toggle = not toggle
            if self.prev_direction:
                key_up(self.prev_direction)


class Adjust(Command):
    """Fine-tunes player position using small movements."""

    def __init__(self, x, y, max_steps=5):
        super().__init__(locals())
        self.target = (float(x), float(y))
        self.max_steps = settings.validate_nonnegative_int(max_steps)


def step(direction, target):
    """
    The default 'step' function. If not overridden, immediately stops the bot.
    :param direction:   The direction in which to move.
    :param target:      The target location to step towards.
    :return:            None
    """

    print("\n[!] Function 'step' not implemented in current command book, aborting process.")
    config.enabled = False


class Wait(Command):
    """Waits for a set amount of time."""

    def __init__(self, duration):
        super().__init__(locals())
        self.duration = float(duration)

    def main(self):
        time.sleep(self.duration)


class Walk(Command):
    """Walks in the given direction for a set amount of time."""

    def __init__(self, direction, duration):
        super().__init__(locals())
        self.direction = settings.validate_horizontal_arrows(direction)
        self.duration = float(duration)

    def main(self):
        key_down(self.direction)
        time.sleep(self.duration)
        key_up(self.direction)
        time.sleep(0.05)


class Fall(Command):
    """
    Performs a down-jump and then free-falls until the player exceeds a given distance
    from their starting position.
    """

    def __init__(self, distance=settings.move_tolerance / 2):
        super().__init__(locals())
        self.distance = float(distance)

    def main(self):
        start = config.player_pos
        key_down('down')
        time.sleep(0.05)
        if config.stage_fright and utils.bernoulli(0.5):
            time.sleep(utils.rand_float(0.2, 0.4))
        counter = 6
        while config.enabled and \
                counter > 0 and \
                utils.distance(start, config.player_pos) < self.distance:
            press('space', 1, down_time=0.1)
            counter -= 1
        key_up('down')
        time.sleep(0.05)


class Buff(Command):
    """Undefined 'buff' command for the default command book."""

    def main(self):
        print(
            "\n[!] 'Buff' command not implemented in current command book, aborting process.")
        config.enabled = False
