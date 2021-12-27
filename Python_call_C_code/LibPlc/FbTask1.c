#include <math.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include "FbTask1.h"

void FbTask1(struct DbTask1 *p)
{
uint32_t Ts_ms = p->Ts_ms; //Шаг дискретизации по времени [мс].
bool     Reset = p->Reset; //Сброс при перезагрузке.
printf("gcc: call FbTask1. Ts_ms: %d \n", Ts_ms);
printf("gcc: call FbTask1. Reset: %d \n", Reset);
return;
}
