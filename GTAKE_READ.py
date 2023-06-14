"""
VFD GTAKE GK820-4T37B read default parameters
Клеммы 485+ 485-
По умолчанию.
RS485 MODBUS RTU 9600 8N2
MODBUS ADDRESS 1
FUNCTION 3 READ HOLDING REGISTER
REGISTER ADDRESS 0x1F02 = 7938 (uint16) U0-02 Напряжение в звене постоянного тока 530VAC
"""

import minimalmodbus

client = minimalmodbus.Instrument('com3', 1) # port, slave address
client.serial.baudrate = 9600
client.serial.bytesize = 8
client.serial.parity = minimalmodbus.serial.PARITY_NONE
client.serial.stopbits = 2
client.serial.timeout = 1
#client.serial.timeout  = 0.05          # seconds

print("Start read parameters")

def Print_register_value(Holding_register = 7938):
    response = client.read_registers(Holding_register, 1) #adr, count
    if response is None:
        print("R", hex(Holding_register), "= Error read 1")
    else:
        print("R", hex(Holding_register), "=", response)

i = 0
#for i in range(0xffff):
while(i < 0x6500):
    try:
        Print_register_value(i)
        i = i + 1 #next param
    except:
        print("R", hex(i), "= Error read 2")
        i = (i + 0x100) & 0xff00 #next group param

client.serial.close()
print("Stop read parameters")
input("Press any key...")
