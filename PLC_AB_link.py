#!/usr/bin/python3
# -*- coding: utf-8 -*-
# https://habr.com/ru/articles/783908/

try:
    import pycomm3
except:
    import os
    os.system("python.exe -m pip install --upgrade pip")
    os.system("pip3 install pycomm3")
    import pycomm3

class PLC_Allen_Bradley_link(object):
    """ Read data from PLC Allen Bradley """
    
    def __init__(self) -> None:
        self.PLC_IP = str('192.168.202.10')
        self.PLC = pycomm3.LogixDriver(self.PLC_IP)
        self.PLC.open()
        print(self.PLC) # Program Name: RS_3000, Revision: {'major': 20, 'minor': 14}
        return
    
    def read_tag(self, tag_name :str = 'b_23'):
        plc_tag_struct = self.PLC.read(tag_name)
        print(plc_tag_struct) # b_23, False, BOOL, None
        plc_tag_value = plc_tag_struct[1]
        return plc_tag_value
    
    def __del__(self) -> None:
        self.PLC.close()
        del self
        return

if __name__ == "__main__":
    PLC = PLC_Allen_Bradley_link()
    print("PLC Tag 'b_23' =", PLC.read_tag(tag_name = 'b_23'))
    del PLC
    input("Press any key for exit...")

# Python 3.11.2
# Program Name: RS_3000, Revision: {'major': 20, 'minor': 14}
# b_23, False, BOOL, None
# PLC Tag 'b_23' = False
# Press any key for exit...

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
