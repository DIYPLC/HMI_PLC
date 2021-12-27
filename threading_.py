# -*- coding: utf-8 -*-

import threading
import time

EN = bool(True)
Counter1 = int(0)

def thread1(): #REPL runtime debug
    while EN:
        try:
            print(eval(input("thread for eval >>>")))
        except:
            print("Error python command")
    return

def thread2():
    while EN:
        global Counter1
        Counter1 = Counter1 + 100
        time.sleep(0.1)
    return

def loop():
    while EN:
        time.sleep(1.0)
    return

def setup():
    thread_2 = threading.Thread(target = thread2)
    thread_1 = threading.Thread(target = thread1)
    thread_2.start()
    thread_1.start()
    return

def OFF():
    global EN
    EN = False
    return

if (__name__ == '__main__'):
    setup()
    loop()
    print("main exit")





