from ctypes import *
import os.path
import sys


def test(c):
    print ("test before ")
    print (id(c))
    c += 2
    print ("test after +")
    print (id(c))
    return c


def printIt(t):
    for i in range(len(t)):
        print (t[i])


if __name__ == "__main__":
    a = 2
    print ("main before invoke test")
    print (id(a))
    n = test(a)
    print ("main afterf invoke test")
    print (a)
    print (id(a))