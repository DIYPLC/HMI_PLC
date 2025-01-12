import os
try: #импортируем библиотеку
    import matplotlib.pyplot
except: #если нет библиотеки качаем ее из интернета и пробуем еще раз
    os.system("pip install matplotlib")
    import matplotlib.pyplot

ys = [16,9,4,1,0,1,4,9,16]
xs = [-4,-3,-2,-1,0,1,2,3,4]
matplotlib.pyplot.plot(xs,ys)
matplotlib.pyplot.title("title")
matplotlib.pyplot.xlabel("xlabel")
matplotlib.pyplot.ylabel("ylabel")
matplotlib.pyplot.scatter(0,1)
#matplotlib.pyplot.axis([-5,5,0,20])
matplotlib.pyplot.show()

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
