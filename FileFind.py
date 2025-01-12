#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

FindFile = "Приказ"
path ="C:/"

filelist = []

for root, dirs, files in os.walk(path):
    for file in files:
        FullPath = os.path.join(root,file)
        #filelist.append(FullPath)
        if (FullPath.find(FindFile) != -1):
            print(FullPath)


"""
for name in filelist:
    print(name)
"""

input("press any key")

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
