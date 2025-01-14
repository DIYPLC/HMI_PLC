#include <stdint.h>
#include <stdbool.h>
#include <iso646.h>
#include <math.h>
#include <stdio.h>
#include "FbPyTask.h"

#define Ts_ms p->Ts_ms
#define Reset p->Reset
#define MW0 p->MW0
#define MW1 p->MW1
#define MW2 p->MW2

void FbPyTask(struct DbPyTask *p)
{
printf("gcc: call FbPyTask.c Ts_ms: %d \n", Ts_ms);
printf("gcc: call FbPyTask.c Reset: %d \n", Reset);
MW2 = MW0 + MW1;
return;
}

// Example one way interface
bool Read_bool(void) { return true; }
uint8_t Read_uint8_t(void) { return  8; }
uint16_t Read_uint16_t(void) { return 16; }
uint32_t Read_uint32_t(void) { return 32; }
uint64_t Read_uint64_t(void) { return 64; }
int8_t Read_int8_t(void) { return  -8; }
int16_t Read_int16_t(void) { return -16; }
int32_t Read_int32_t(void) { return -32; }
int64_t Read_int64_t(void) { return -64; }
float Read_float(void) { return 3.2; }
double Read_double(void) { return 6.4; }
void Write_bool(bool in) { printf("gcc: bool %d \n",in); return; }
void Write_uint8_t(uint8_t in) { printf("gcc: uint8_t %d \n",in); return; }
void Write_uint16_t(uint16_t in) { printf("gcc: uint16_t %d \n",in); return; }
void Write_uint32_t(uint32_t in) { printf("gcc: uint32_t %d \n",in); return; }
void Write_uint64_t(uint64_t in) { printf("gcc: uint64_t %d \n",((int)in)); return; }
void Write_int8_t(int8_t in) { printf("gcc: int8_t %d \n",in); return; }
void Write_int16_t(int16_t in) { printf("gcc: int16_t %d \n",in); return; }
void Write_int32_t(int32_t in) { printf("gcc: int32_t %d \n",in); return; }
void Write_int64_t(int64_t in) { printf("gcc: int64_t %d \n",((int)in)); return; }
void Write_float(float in) { printf("gcc: float %f \n",in); return; }
void Write_double(double in) { printf("gcc: double %f \n",in); return; }

// @COPYLEFT ALL WRONGS RESERVED :)
// Author: VA
// Contacts: DIY.PLC.314@gmail.com
// Date start LIB_PLC: 2014
// License: GNU GPL-2.0-or-later
// https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
// https://www.youtube.com/watch?v=n1F_MfLRlX0
// https://www.youtube.com/@DIY_PLC
// https://github.com/DIYPLC/LIB_PLC
// https://oshwlab.com/diy.plc.314/PLC_HW1_SW1
// https://3dtoday.ru/3d-models/mechanical-parts/body/korpus-na-din-reiku
// https://t.me/DIY_PLC
