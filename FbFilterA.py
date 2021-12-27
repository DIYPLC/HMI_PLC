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


