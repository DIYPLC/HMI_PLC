# -*- coding: utf-8 -*-

#Фильтр апериодический.
#      DbFilterA
#    +-----------+
#    | FbFilterA |
# ->-|In      Out|->-
#   -|Tf         |
#   -|Ts         |
#    +-----------+

class FbFilterA():
    #Входные переменные, сохраняемые.
    In = float(0.0); #Входной сигнал до фильтрации.
    Tf = float(1.0); #Постоянная времени фильтра [с].
    Ts = float(0.1); #Шаг дискретизации по времени [с].
    #Выходные переменные, сохраняемые.
    Out = float(0.0); #Выходной сигнал после фильтрации.
    #Фильтрация
    def execute(self):
        #Внутренние переменные, не сохраняемые.
        Tmp = float(0.0);
        #W(s) = 1/(1+Tf*s) при Ts->0.
        if (self.Tf <= 0.0):
            self.Out = self.In;
        else:
            Tmp = (self.In - self.Out) / self.Tf;
            self.Out = self.Out + Tmp * self.Ts;
        return

def Unit_test():
    DbFilterA1 = FbFilterA()
    DbFilterA1.In = 1.0
    Timer1 = 0.0
    for i in range(15):
        print("T:",Timer1,"Out:",DbFilterA1.Out)
        DbFilterA1.execute()
        Timer1 = Timer1 + 0.1

if (__name__ == '__main__'):
    Unit_test()
    input("press any key ")

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
# Date: 2014 - 2024
# License: GNU GPL-2.0-or-later
# https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# https://www.youtube.com/watch?v=n1F_MfLRlX0
#
# See also:
# https://www.youtube.com/@DIY_PLC
# https://github.com/DIYPLC/LIB_PLC
# https://oshwlab.com/diy.plc.314/PLC_HW1_SW1
# https://3dtoday.ru/3d-models/mechanical-parts/body/korpus-na-din-reiku
# https://t.me/DIY_PLC
