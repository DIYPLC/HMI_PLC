#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
SOFT PLC
Python 3.12.2
Windows 10 Pro x64
Ubuntu 20.04.6 LTS + Python 3.8.10
08-04-2025
"""

import time
import gc,importlib,os
import socket
import threading


def error_generator():
    return 0 / 0


def auto_restart_plc() -> None:
    """" Этот метод работает но приводит к утечке памяти. """
    """ Возможно лучше перезагрузить OS. """
    print("auto_restart_plc()")
    if os.name == 'posix':
        os.system("python3 __main__.py")
    else: # os.name == 'nt'
        os.system("__main__.py")
    return


def reboot_windows() -> None:
    import os
    import time
    print("shutdown /r /f /t 60")
    time.sleep(5*60)
    os.system("shutdown /r /f /t 60") #60s delay
    time.sleep(90)
    return


class InterProcessCommunication(object):
    """ Shared memory for IPC """
    
    def __init__(self) -> None:
        #print("IPC __init__()")
        self.Stop_Thread1 = bool(True)
        self.Stop_Task1 = bool(False)
        return
    
    def __call__(self) -> None:
        #print("IPC __call__()")
        self.Thread1 = threading.Thread(target=fc_thread1)
        self.Thread1.start()
        return
    
    def __enter__(self) -> None:
        #print("IPC __enter__()")
        return
    
    def __exit__(self) -> None:
        #print("IPC __exit__()")
        #self.__del__()
        return
   
    def __del__(self) -> None:
        #print("IPC __del__()")
        del self
        return


def fc_thread1(): # TODO
    while True:
        if IPC.Stop_Thread1:
            break
        time.sleep(5.0)
        print("threading run")
    return


if __name__ == "__main__":
    while True:
        try:
            from Write_to_Error_file import write_to_error_file
            from Task1 import Task1
            write_to_error_file("[OK] START __main__.py ")
            IPC = InterProcessCommunication()
            IPC()
            DbTask1 = Task1()
            DbTask1.setup()
            while True:
                DbTask1.loop()
                if IPC.Stop_Task1:
                    write_to_error_file("[ERR] STOP Task1.py")
                    break
        except BaseException as error:
            print("[ERR] delay")
            write_to_error_file("[ERR] __main__.py " + str(error))
            IPC.Stop_Thread1 = True
            time.sleep(10)
            del DbTask1
            del Task1
            del IPC
            importlib.reload(socket)
            importlib.reload(threading)
            gc.collect()
            #auto_restart_plc()
    print("[ERR] STOP __main__ " + time.strftime("%d-%b-%Y %H:%M:%S"))


# @COPYLEFT ALL WRONGS RESERVED :)
# Author: VA
# Contacts: DIY.PLC.314@gmail.com
# Date start LIB_PLC: 2014
# License: GNU GPL-2.0-or-later
# https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# https://www.youtube.com/watch?v=n1F_MfLRlX0
# https://www.youtube.com/@DIY_PLC
# https://github.com/DIYPLC/LIB_PLC
# https://oshwlab.com/diy.plc.314/PLC_HW1_SW1
# https://3dtoday.ru/3d-models/mechanical-parts/body/korpus-na-din-reiku
# https://t.me/DIY_PLC
