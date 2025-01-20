#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
try:
    import tkinter
except BaseException:
    print("ERROR import tkinter")
    print("sudo apt-get install python3-tk")
    input("Press any key for exit...")



class GlobalVarGui(object):

    def __init__(self) -> None:
        self._color_bg_1_ = "#D4D0C8"
        self._color_bg_2_ = "#A9A9A9"
        # root
        self.root = tkinter.Tk()
        self.root.title("GUI python3 tkinter")
        #self.root.geometry("400x300")
        self.root.resizable(False, False)
        # Frame_main
        self.Frame_main = tkinter.Frame(self.root)
        self.Frame_main["borderwidth"] = 2
        self.Frame_main["relief"] = tkinter.RIDGE
        self.Frame_main["background"] = self._color_bg_1_
        self.Frame_main.grid(column = 0, row =0, sticky = "w,e")
        # Label1
        self.Label1 = tkinter.Label(self.Frame_main)
        self.Label1["text"] = "Label1"
        self.Label1["font"] = "Monospace 12"
        self.Label1.grid(column=0, row=0, sticky="w,e")
        # Entry1
        self.Entry1_value = tkinter.StringVar()
        self.Entry1 = tkinter.Entry(self.Frame_main)
        self.Entry1.configure(textvariable=self.Entry1_value)
        self.Entry1.bind("<Return>", action_enter_entry1)
        self.Entry1.configure(width=30)
        self.Entry1.configure(font="Monospace 12")
        self.Entry1.grid(column=0, row=1, sticky="w,e")
        # Button1
        self.Button1 = tkinter.Button(self.Frame_main)
        self.Button1.configure(text="Button1")
        self.Button1.configure(height=1)
        self.Button1.configure(width=30)
        self.Button1.configure(font="Monospace 12")
        self.Button1.configure(command=action_press_button1)
        self.Button1.grid(column=0, row=2, sticky="w,e")
        return

    def __del__(self) -> None:
        del self
        return


def cyclic_call_1000_ms() -> None:
    GUI.Label1["text"] = time.strftime("%H:%M:%S")
    GUI.root.after(1000, cyclic_call_1000_ms)

def action_press_button1() -> None:
    print("GUI press Button1 " + time.strftime("%H:%M:%S"))
    return

def action_enter_entry1(self) -> None:
    tmp = str(GUI.Entry1_value.get())
    print("GUI press Enter Entry1", tmp)
    return

if __name__ == "__main__":
    print("GUI start " + time.strftime("%H:%M:%S"))
    GUI = GlobalVarGui()
    cyclic_call_1000_ms()
    GUI.root.mainloop()
    print("GUI stop " + time.strftime("%H:%M:%S"))

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
