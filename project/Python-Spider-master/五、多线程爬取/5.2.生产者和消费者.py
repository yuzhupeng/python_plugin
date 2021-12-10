
import threading
import random,time

gMoney = 1000
gLock = threading.Lock()
gTotalTimes = 10
gTimes = 0


class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTimes
        while True:
            money = random.randint(100,1000)
            gLock.acquire()
            #只生产10次，超过就停止，必须把锁给释放掉，否则产生死锁
            if gTimes >= gTotalTimes:
                gLock.release()
                break
            gMoney += money
            print('%s生产了%d元钱,剩余%d元钱' % (threading.current_thread(), money, gMoney))
            #生产一次，次数加1，总共10次
            gTimes += 1
            gLock.release()
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(100,1000)
            gLock.acquire()
            if gMoney >= money:
                gMoney -= money
                print('%s消费了%d元钱,剩余%d元钱' % (threading.current_thread(), money,gMoney))
            else:
                if gTimes >= gTotalTimes:
                    gLock.release()
                    break
            gLock.release()
            time.sleep(0.5)


def main():
    for x in range(5):
        t1 = Producer()
        t1.start()

    for x in range(2):
        t2 = Consumer()
        t2.start()

if __name__ == '__main__':
    main()