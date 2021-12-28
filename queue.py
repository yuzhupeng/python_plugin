#导入模块
from multiprocessing import  Queue
from threading import Thread

import time

#创建生产者
def producer(q):
    print("start producer")
    for i in range(10):
        q.put(i)              #发消息
        print(f'生产消息：{i}')
        time.sleep(0.5)
    print("end producer")

#创建消费者，消费者一般是个死循环，要一直监听是否有需要处理的信息。
def customer(q):
    print("start customer")
    while 1:
        data = q.get()        #收消息
        print("customer has get value {0}".format(data))


if __name__ == '__main__':
    q = Queue()                           #创建一个队列
    pro = Thread(target=producer,args=(q,))
    cus = Thread(target=customer,args=(q,))
    pro.start()
    cus.start()