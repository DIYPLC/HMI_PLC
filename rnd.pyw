"""
Генератотар случайных чисел от 0 до 255
Генерирует шеснадцатиричный байт по случайноу нажатию кнопки.
По нажатию кнопки отображает слуачное число и записывает случайные числа в текстовый файл.
08-06-2023
Windows 10
Python 3.11
"""

import tkinter
import threading

class Global_var:
    window = tkinter.Tk()# окно
    label_number = tkinter.Label(window)# виджет
    Button_random = tkinter.Button(window)# кнопка
    chislo = 0# переменная
    stop_thread = False

# добавляем функцию с реакцией на нажатие
def Button_on (event):
    with open("random.txt","a") as r_h: #пишем в файл
        tmp = (str(hex(Global_var.chislo)))
        tmp = tmp[2:]# отрезаем 2 первых символа
        r_h.write(tmp)# добавляем байт в файл 
    Global_var.label_number.configure(text = tmp)# выводим число в приложении

def GUI():
    # окно 
    Global_var.window.geometry('240x70')# делаем разрешени еокна
    Global_var.window.resizable(False,False)# запрещяем его расширять уменьшать
    Global_var.window.title('Random')# даем название
    Global_var.window['bg'] = '#D4D0D0'# цвет фона
    # виджет числа 
    Global_var.label_number.configure(bg = '#F0F0F0')
    Global_var.label_number.place(x = 10,y = 10, width = 100, height = 50)# даем кординаты и размер 
    Global_var.label_number.configure(text = hex(Global_var.chislo))# даем название 
    Global_var.label_number.configure(font = (20))# размер шрифта
    # кнопка для рамдома 
    Global_var.Button_random.configure(bg = '#E0E0E0')
    Global_var.Button_random.configure(text = 'Random')
    Global_var.Button_random.configure(font = (15))
    Global_var.Button_random.place(x = 130,y = 10, width = 100, height = 50)
    Global_var.Button_random.bind("<Button-1>",Button_on)# добавляем реакцию команды на нажатие

def Counter ():
    while True:# счетчик 0-255
        Global_var.chislo = (Global_var.chislo + 1) & 0xFF
        if (Global_var.stop_thread):
            break
    return

Global_var()
GUI()

Thread_1 = threading.Thread(target = Counter)
Thread_1.start()#запускаем ее

Global_var.window.mainloop()# запуск обработки событий
Global_var.stop_thread = True

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
