#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#include "LibPlc.h"

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
