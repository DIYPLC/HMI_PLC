# -*- coding: utf-8 -*-
import time
import tkinter

class Global_var_for_GUI:
    """Глобальные переменные и классы"""
    root = tkinter.Tk()
    Label1 = tkinter.Label(root)
    Entry1 = tkinter.Entry(root)
    Button1 = tkinter.Button(root)

def FunctionTimeInterrypt1000ms():
    """Функция прерывания каждые 1000мс."""
    #Вывести в текст метки текущее время
    GUI.Label1["text"] = time.strftime("%H:%M:%S") 
    #Выполнить через 1000мс себя же.
    GUI.root.after(1000, FunctionTimeInterrypt1000ms)

def FunctionButton1():
    print("Нажали Кнопку1 в " + time.strftime("%H:%M:%S"))

def Plot_GIU():
    #Окно1
    GUI.root.title("PID control 1PIRCA1")
    GUI.root.geometry("400x300")
    GUI.root.resizable(False, False) #Окно с постоянными размерами
    #Метка1
    GUI.Label1["text"] = "Метка1"
    GUI.Label1["font"] = "Monospace 12"
    GUI.Label1.place(x = 0, y = 20)
    #Поле ввода текста1
    GUI.Entry1.configure(width  = 15)
    GUI.Entry1.configure(font = "Monospace 12")
    GUI.Entry1.place(x = 0, y = 60)
    #Кнопа1
    GUI.Button1.configure(text = "Кнопка1")
    GUI.Button1.configure(height = 1)
    GUI.Button1.configure(width  = 15)
    GUI.Button1.configure(font = "Monospace 12")
    GUI.Button1.configure(command = FunctionButton1)
    GUI.Button1.place(x = 0, y = 100)
    return

print("Начало программы в " + time.strftime("%H:%M:%S"))
GUI = Global_var_for_GUI
Plot_GIU()
FunctionTimeInterrypt1000ms() #Запустить прерывание каждые 1000мс
GUI.root.mainloop()
print("Конец программы в " + time.strftime("%H:%M:%S"))

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
