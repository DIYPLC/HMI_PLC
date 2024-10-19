#https://ru.wikipedia.org/wiki/DTMF
#https://habr.com/ru/post/661037/
#https://play.google.com/store/apps/details?id=com.wolphi.dtmf&hl=ru
#win 10 python3.9

import time

try: 
    import sounddevice as sd
except: #download from internet
    import os
    os.system("pip install sounddevice")
    import sounddevice as sd

try: 
    import numpy as np
except: #download from internet
    import os
    os.system("pip install numpy")
    import numpy as np

SAMPLERATE = 24000 #битрейт 
AMP = 0.5 #амплитуда 
DURATION_PULSE = 1 #длительность сигнала секунд. 80мс минимум по стандарту
DURATION_PAUSE = 0 #Длительнасть паузы в секундах. 10мс минимум пр стандарту

#Гц калибровка неточностей по анализатору спектра или ослику.
F350  = 350 + 28
F440  = 440 + 36
F480  = 480 + 41
F620  = 620 + 57
F697  = 697 + 64
F770  = 770 + 68
F852  = 852 + 76
F941  = 941 + 77
F1209 = 1209 + 110
F1336 = 1336 + 118
F1477 = 1477 + 130
F1633 = 1633 + 140

def GEN_ALIBRATION_TONE():
    SAMPLERATE = 24000 #битрейт 
    AMP = 0.5 #амплитуда 
    DURATION_PULSE = 1 #длительность сигнала секунд. 80мс минимум по стандарту
    F = F1633 #Hz
    t = np.arange(DURATION_PULSE * SAMPLERATE) / (SAMPLERATE * 2) #хз почему.
    signal = AMP  * np.sin(2 * np.pi * F * t)
    sd.play(signal)
    sd.wait()
    return

def DTMF_DELAY():
    time.sleep(DURATION_PAUSE) #Длительнасть паузы в секундах.
    return

def DTMF_PULSE_GEN_SUMBOL_1():
    F1 = F697  #Hz
    F2 = F1209 #Hz
    t = np.arange(DURATION_PULSE * SAMPLERATE) / (SAMPLERATE * 2) #хз почему.
    signal = AMP  * ( np.sin(2 * np.pi * F1 * t) + np.sin(2 * np.pi * F2 * t) )
    sd.play(signal)
    sd.wait()
    return

def DTMF_PULSE_GEN_SUMBOL_2():
    F1 = F697  #Hz
    F2 = F1336 #Hz
    t = np.arange(DURATION_PULSE * SAMPLERATE) / (SAMPLERATE * 2) #хз почему.
    signal = AMP  * ( np.sin(2 * np.pi * F1 * t) + np.sin(2 * np.pi * F2 * t) )
    sd.play(signal)
    sd.wait()
    return

def DTMF_PULSE_GEN_SUMBOL_3():
    F1 = F697  #Hz
    F2 = F1477 #Hz
    t = np.arange(DURATION_PULSE * SAMPLERATE) / (SAMPLERATE * 2) #хз почему.
    signal = AMP  * ( np.sin(2 * np.pi * F1 * t) + np.sin(2 * np.pi * F2 * t) )
    sd.play(signal)
    sd.wait()
    return

def DTMF_PULSE_GEN_SUMBOL_A():
    F1 = F697  #Hz
    F2 = F1633 #Hz
    t = np.arange(DURATION_PULSE * SAMPLERATE) / (SAMPLERATE * 2) #хз почему.
    signal = AMP  * ( np.sin(2 * np.pi * F1 * t) + np.sin(2 * np.pi * F2 * t) )
    sd.play(signal)
    sd.wait()
    return

def DTMF_PULSE_GEN_SUMBOL_4():
    F1 = F770  #Hz
    F2 = F1209 #Hz
    t = np.arange(DURATION_PULSE * SAMPLERATE) / (SAMPLERATE * 2) #хз почему.
    signal = AMP  * ( np.sin(2 * np.pi * F1 * t) + np.sin(2 * np.pi * F2 * t) )
    sd.play(signal)
    sd.wait()
    return

def DTMF_PULSE_GEN_SUMBOL_5():
    F1 = F770  #Hz
    F2 = F1336 #Hz
    t = np.arange(DURATION_PULSE * SAMPLERATE) / (SAMPLERATE * 2) #хз почему.
    signal = AMP  * ( np.sin(2 * np.pi * F1 * t) + np.sin(2 * np.pi * F2 * t) )
    sd.play(signal)
    sd.wait()
    return

def DTMF_PULSE_GEN_SUMBOL_6():
    F1 = F770  #Hz
    F2 = F1477 #Hz
    t = np.arange(DURATION_PULSE * SAMPLERATE) / (SAMPLERATE * 2) #хз почему.
    signal = AMP  * ( np.sin(2 * np.pi * F1 * t) + np.sin(2 * np.pi * F2 * t) )
    sd.play(signal)
    sd.wait()
    return

def DTMF_PULSE_GEN_SUMBOL_B():
    F1 = F770  #Hz
    F2 = F1633 #Hz
    t = np.arange(DURATION_PULSE * SAMPLERATE) / (SAMPLERATE * 2) #хз почему.
    signal = AMP  * ( np.sin(2 * np.pi * F1 * t) + np.sin(2 * np.pi * F2 * t) )
    sd.play(signal)
    sd.wait()
    return

def DTMF_PULSE_GEN_SUMBOL_7():
    F1 = F852  #Hz
    F2 = F1209 #Hz
    t = np.arange(DURATION_PULSE * SAMPLERATE) / (SAMPLERATE * 2) #хз почему.
    signal = AMP  * ( np.sin(2 * np.pi * F1 * t) + np.sin(2 * np.pi * F2 * t) )
    sd.play(signal)
    sd.wait()
    return

def DTMF_PULSE_GEN_SUMBOL_8():
    F1 = F852  #Hz
    F2 = F1336 #Hz
    t = np.arange(DURATION_PULSE * SAMPLERATE) / (SAMPLERATE * 2) #хз почему.
    signal = AMP  * ( np.sin(2 * np.pi * F1 * t) + np.sin(2 * np.pi * F2 * t) )
    sd.play(signal)
    sd.wait()
    return

def DTMF_PULSE_GEN_SUMBOL_9():
    F1 = F852  #Hz
    F2 = F1477 #Hz
    t = np.arange(DURATION_PULSE * SAMPLERATE) / (SAMPLERATE * 2) #хз почему.
    signal = AMP  * ( np.sin(2 * np.pi * F1 * t) + np.sin(2 * np.pi * F2 * t) )
    sd.play(signal)
    sd.wait()
    return

def DTMF_PULSE_GEN_SUMBOL_C():
    F1 = F852  #Hz
    F2 = F1633 #Hz
    t = np.arange(DURATION_PULSE * SAMPLERATE) / (SAMPLERATE * 2) #хз почему.
    signal = AMP  * ( np.sin(2 * np.pi * F1 * t) + np.sin(2 * np.pi * F2 * t) )
    sd.play(signal)
    sd.wait()
    return

def DTMF_PULSE_GEN_SUMBOL_STAR():
    F1 = F941  #Hz
    F2 = F1209 #Hz
    t = np.arange(DURATION_PULSE * SAMPLERATE) / (SAMPLERATE * 2) #хз почему.
    signal = AMP  * ( np.sin(2 * np.pi * F1 * t) + np.sin(2 * np.pi * F2 * t) )
    sd.play(signal)
    sd.wait()
    return

def DTMF_PULSE_GEN_SUMBOL_0():
    F1 = F941  #Hz
    F2 = F1336 #Hz
    t = np.arange(DURATION_PULSE * SAMPLERATE) / (SAMPLERATE * 2) #хз почему.
    signal = AMP  * ( np.sin(2 * np.pi * F1 * t) + np.sin(2 * np.pi * F2 * t) )
    sd.play(signal)
    sd.wait()
    return

def DTMF_PULSE_GEN_SUMBOL_SHARP():
    F1 = F941  #Hz
    F2 = F1477 #Hz
    t = np.arange(DURATION_PULSE * SAMPLERATE) / (SAMPLERATE * 2) #хз почему.
    signal = AMP  * ( np.sin(2 * np.pi * F1 * t) + np.sin(2 * np.pi * F2 * t) )
    sd.play(signal)
    sd.wait()
    return

def DTMF_PULSE_GEN_SUMBOL_D():
    F1 = F941  #Hz
    F2 = F1633 #Hz
    t = np.arange(DURATION_PULSE * SAMPLERATE) / (SAMPLERATE * 2) #хз почему.
    signal = AMP  * ( np.sin(2 * np.pi * F1 * t) + np.sin(2 * np.pi * F2 * t) )
    sd.play(signal)
    sd.wait()
    return

def DTMF_PULSE_GEN_SUMBOL_BUSY():
    F1 = F480 #Hz
    F2 = F620 #Hz
    t = np.arange(DURATION_PULSE * SAMPLERATE) / (SAMPLERATE * 2) #хз почему.
    signal = AMP  * ( np.sin(2 * np.pi * F1 * t) + np.sin(2 * np.pi * F2 * t) )
    sd.play(signal)
    sd.wait()
    return

def DTMF_PULSE_GEN_SUMBOL_READY():
    F1 = F350 #Hz
    F2 = F440 #Hz
    t = np.arange(DURATION_PULSE * SAMPLERATE) / (SAMPLERATE * 2) #хз почему.
    signal = AMP  * ( np.sin(2 * np.pi * F1 * t) + np.sin(2 * np.pi * F2 * t) )
    sd.play(signal)
    sd.wait()
    return

def DTMF_PULSE_GEN_SUMBOL_RINGBACK():
    F1 = F440 #Hz
    F2 = F480 #Hz
    t = np.arange(DURATION_PULSE * SAMPLERATE) / (SAMPLERATE * 2) #хз почему.
    signal = AMP  * ( np.sin(2 * np.pi * F1 * t) + np.sin(2 * np.pi * F2 * t) )
    sd.play(signal)
    sd.wait()
    return

#GEN_ALIBRATION_TONE()

DTMF_PULSE_GEN_SUMBOL_0()
DTMF_DELAY()
DTMF_PULSE_GEN_SUMBOL_1()
DTMF_DELAY()
DTMF_PULSE_GEN_SUMBOL_2()
DTMF_DELAY()
DTMF_PULSE_GEN_SUMBOL_3()
DTMF_DELAY()
DTMF_PULSE_GEN_SUMBOL_4()
DTMF_DELAY()
DTMF_PULSE_GEN_SUMBOL_5()
DTMF_DELAY()
DTMF_PULSE_GEN_SUMBOL_6()
DTMF_DELAY()
DTMF_PULSE_GEN_SUMBOL_7()
DTMF_DELAY()
DTMF_PULSE_GEN_SUMBOL_8()
DTMF_DELAY()
DTMF_PULSE_GEN_SUMBOL_9()
DTMF_DELAY()
DTMF_PULSE_GEN_SUMBOL_A()
DTMF_DELAY()
DTMF_PULSE_GEN_SUMBOL_B()
DTMF_DELAY()
DTMF_PULSE_GEN_SUMBOL_C()
DTMF_DELAY()
DTMF_PULSE_GEN_SUMBOL_D()
DTMF_DELAY()
DTMF_PULSE_GEN_SUMBOL_STAR()
DTMF_DELAY()
DTMF_PULSE_GEN_SUMBOL_SHARP()

#DTMF_DELAY()
#DTMF_PULSE_GEN_SUMBOL_BUSY()
#DTMF_DELAY()
#DTMF_PULSE_GEN_SUMBOL_READY()
#DTMF_DELAY()
#DTMF_PULSE_GEN_SUMBOL_RINGBACK()

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
