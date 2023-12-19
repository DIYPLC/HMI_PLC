#!/usr/bin/python
# -*- coding: utf-8 -*-

# Преобразование слова в 16 бит.
#      DbWordToBits
#    +--------------+
#    | FbWordToBits |
# ->-|In        Out0|->-
#    |          Out1|->-
#    |          Out2|->-
#    |          Out3|->-
#    |          Out4|->-
#    |          Out5|->-
#    |          Out6|->-
#    |          Out7|->-
#    |          Out8|->-
#    |          Out9|->-
#    |         Out10|->-
#    |         Out11|->-
#    |         Out12|->-
#    |         Out13|->-
#    |         Out14|->-
#    |         Out15|->-
#    +--------------+


class FbWordToBits():
    def __init__(self): #Auto init VAR
        #Входные переменные, сохраняемые.
        self.In = 0
        #Выходные переменные, сохраняемые.
        self.Out0 = False
        self.Out1 = False
        self.Out2 = False
        self.Out3 = False
        self.Out4 = False
        self.Out5 = False
        self.Out6 = False
        self.Out7 = False
        self.Out8 = False
        self.Out9 = False
        self.Out10 = False
        self.Out11 = False
        self.Out12 = False
        self.Out13 = False
        self.Out14 = False
        self.Out15 = False
        #Внутренние переменные, сохраняемые.
        return
    def Run(self):
        self.Out0  = bool(self.In & 0b0000000000000001)
        self.Out1  = bool(self.In & 0b0000000000000010)
        self.Out2  = bool(self.In & 0b0000000000000100)
        self.Out3  = bool(self.In & 0b0000000000001000)
        self.Out4  = bool(self.In & 0b0000000000010000)
        self.Out5  = bool(self.In & 0b0000000000100000)
        self.Out6  = bool(self.In & 0b0000000001000000)
        self.Out7  = bool(self.In & 0b0000000010000000)
        self.Out8  = bool(self.In & 0b0000000100000000)
        self.Out9  = bool(self.In & 0b0000001000000000)
        self.Out10 = bool(self.In & 0b0000010000000000)
        self.Out11 = bool(self.In & 0b0000100000000000)
        self.Out12 = bool(self.In & 0b0001000000000000)
        self.Out13 = bool(self.In & 0b0010000000000000)
        self.Out14 = bool(self.In & 0b0100000000000000)
        self.Out15 = bool(self.In & 0b1000000000000000)
        return
    def Set_In(self, Value: int):
        self.In = int(Value)
        return
    def Get_Out0(self) -> bool:
        return bool(self.Out0)
    def Get_Out1(self) -> bool:
        return bool(self.Out1)
    def Get_Out2(self) -> bool:
        return bool(self.Out2)
    def Get_Out3(self) -> bool:
        return bool(self.Out3)
    def Get_Out4(self) -> bool:
        return bool(self.Out4)
    def Get_Out5(self) -> bool:
        return bool(self.Out5)
    def Get_Out6(self) -> bool:
        return bool(self.Out6)
    def Get_Out7(self) -> bool:
        return bool(self.Out7)
    def Get_Out8(self) -> bool:
        return bool(self.Out8)
    def Get_Out9(self) -> bool:
        return bool(self.Out9)
    def Get_Out10(self) -> bool:
        return bool(self.Out10)
    def Get_Out11(self) -> bool:
        return bool(self.Out11)
    def Get_Out12(self) -> bool:
        return bool(self.Out12)
    def Get_Out13(self) -> bool:
        return bool(self.Out13)
    def Get_Out14(self) -> bool:
        return bool(self.Out14)
    def Get_Out15(self) -> bool:
        return bool(self.Out15)

def Unit_test():
    print("Unit test start")
    from FbBitsToWord import FbBitsToWord
    DbWordToBits = FbWordToBits()
    DbBitsToWord = FbBitsToWord()
    Error_flag = False
    for i in range(65536):
        DbWordToBits.In = i
        DbWordToBits.Run()
        DbBitsToWord.In0 = DbWordToBits.Out0
        DbBitsToWord.In1 = DbWordToBits.Out1
        DbBitsToWord.In2 = DbWordToBits.Out2
        DbBitsToWord.In3 = DbWordToBits.Out3
        DbBitsToWord.In4 = DbWordToBits.Out4
        DbBitsToWord.In5 = DbWordToBits.Out5
        DbBitsToWord.In6 = DbWordToBits.Out6
        DbBitsToWord.In7 = DbWordToBits.Out7
        DbBitsToWord.In8 = DbWordToBits.Out8
        DbBitsToWord.In9 = DbWordToBits.Out9
        DbBitsToWord.In10 = DbWordToBits.Out10
        DbBitsToWord.In11 = DbWordToBits.Out11
        DbBitsToWord.In12 = DbWordToBits.Out12
        DbBitsToWord.In13 = DbWordToBits.Out13
        DbBitsToWord.In14 = DbWordToBits.Out14
        DbBitsToWord.In15 = DbWordToBits.Out15
        DbBitsToWord.Run()
        #print(hex(i), hex(DbBitsToWord.Out), hex(DbWordToBits.In))
        if (DbBitsToWord.Out != DbWordToBits.In):
            Error_flag = True
    if (Error_flag):
        print("Test ERROR")
    else:
        print("Test OK")
    return

if (__name__ == "__main__"):
    Unit_test()
    input("press any key for exit...")

#  +---------+
#  | GNU GPL |
#  +---------+
#  |
#  |
#  .= .-_-. =.
# ((_/)o o(\_))
#  `-'(. .)`-'
#  |/| \_/ |\
#  ( |     | )
#  /"\_____/"\
#  \__)   (__/
# @COPYLEFT ALL WRONGS RESERVED :)
# Author: VA
# Contacts: DIY.PLC.314@gmail.com
# License: GNU GPL v2
#
# https://www.youtube.com/@DIY_PLC
# https://github.com/DIYPLC

