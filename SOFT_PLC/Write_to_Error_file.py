#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time

def write_to_error_file(text: str = "text") -> None:
    # Записываем ошибки в файл если файл слишком большой стираем его и пишем в чистый файл.
    file_name = str("Error.txt")
    max_file_size_bytes = int(4096)
    text = str(time.strftime("%d-%b-%Y %H:%M:%S") + ' ' + str(text) + '\n')
    try:  # Получить размер файла в байтах.
        file_size_bytes = os.path.getsize(file_name)
    except BaseException:  # если нет такого файла то размер его 0.
        file_size_bytes = 0
    if file_size_bytes < max_file_size_bytes:  # Ограничим размер файла.
        f = open(file_name, 'a')  # Дописать текст в файл если нет создать.
    else:
        f = open(file_name, 'w')  # Записать в пустой файл.
    print(text)
    f.write(text)
    f.close()
    return

def _unit_test_():
    write_to_error_file("Unit test for error file")
    return

if __name__ == "__main__":
    _unit_test_()
    input("press any key for exit...")

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
