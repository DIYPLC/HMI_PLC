import csv

def Write_csv_file():
    with open('Trend.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['SP', 'PV', 'OP'])
        writer.writerow(['0.0', '0.0', '0.0'])
        writer.writerow(['50.0', '49.9', '25.0'])
    return

def Read_csv_file():
    with open('Trend.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
    return

Write_csv_file()
Read_csv_file()
input()

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
