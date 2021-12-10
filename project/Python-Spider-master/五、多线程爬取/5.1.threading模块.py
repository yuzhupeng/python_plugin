
import threading,time

def coding():
    for x in range(3):
        print('正在写代码%s'%x)
        time.sleep(2)

def drawing():
    for x in range(3):
        print('正在画画%s'%x)
        time.sleep(2)

def main():
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=drawing)
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()

