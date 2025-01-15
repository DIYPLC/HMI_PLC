#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time

def write_to_error_file(text: str = "text") -> None:
    # Записываем ошибки в файл если файл слишком большой стираем его и пишем в чистый файл.
    _FILE_NAME = "Error.txt"
    _MAX_FILE_SIZE_BYTES = 4096
    _TEXT = str(time.strftime("%d-%b-%Y %H:%M:%S")) + ' ' + str(text) + '\n'
    try:  # Получить размер файла в байтах.
        file_size_bytes = os.path.getsize(_FILE_NAME)
    except BaseException:  # если нет такого файла то размер его 0.
        file_size_bytes = 0
    if file_size_bytes < _MAX_FILE_SIZE_BYTES:  # Ограничим размер файла.
        f = open(_FILE_NAME, 'a')  # Дописать текст в файл если нет создать.
    else:
        f = open(_FILE_NAME, 'w')  # Записать в пустой файл.
    print(_TEXT)
    f.write(_TEXT)
    f.close()
    return

def unit_test():
    write_to_error_file("Unit test for error file")
    return

if __name__ == "__main__":
    unit_test()
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
