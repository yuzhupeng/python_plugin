# -*- coding: utf-8 -*-
 


class Arrays(object):
    
    def __init__(self, size=32):
        """
        :param size: 长度
        """
        self._size = size
        self._items = [None] * size

    # 在执行array[key]时执行
    def __getitem__(self, index):
        return self._items[index]

    # 在执行array[key] = value 时执行
    def __setitem__(self, index, value):
        self._items[index] = value

    # 在执行len(array) 时执行
    def __len__(self):
        return self._size
    
    # 清空数组
    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    # 在遍历时执行
    def __iter__(self):
        for item in self._items:
            yield item
            
            
            

a=Arrays(10)
a.__setitem__(1,1)
a.__setitem__(2,3)
a.__setitem__(3,4)
a.__setitem__(4,5)
a.__setitem__(5,5)
a.__setitem__(6,5)

b=a.__iter__()
for i in b:
    print(i)
    
print(next(b))

print(a.__getitem__(5))
a=input()