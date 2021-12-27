#include <math.h>
#include <stdbool.h>
#include <stdint.h>
#include "FbGSS.h"

void FbGss(struct DbGSS *p)
{
  //Входные переменные, сохраняемые.
  float Amplitude = p->Amplitude;
  float Period = p->Period;
  float Phase = p->Phase;
  float Offset = p->Offset;
  float PulseTime = p->PulseTime;
  float Ts = p->Ts;
  //Выходные переменные, сохраняемые.
  float Sine = p->Sine;
  float Cosine = p->Cosine;
  float RectangleR = p->RectangleR;
  bool  RectangleB = p->RectangleB;
  float Triangle = p->Triangle;
  float Prnd = p->Prnd;
  //Внутренние переменные, сохраняемые.
  float    CurrentTime = p->CurrentTime;
  float    IntegratorTriangle = p->IntegratorTriangle;
  uint32_t SummatorRnd = p->SummatorRnd;

  Sine =   Amplitude * sinf(2 * M_PI * (1.0 / Period) * CurrentTime + Phase) + Offset; //Синус.
  Cosine = Amplitude * cosf(2 * M_PI * (1.0 / Period) * CurrentTime + Phase) + Offset; //Косинус.

  if (CurrentTime < PulseTime) //Прямоугольные импульсы.
  {
    RectangleR = Amplitude + Offset;
    RectangleB = true;
  }
  else
  {
    RectangleR = Offset;
    RectangleB = false;
  }

  if (CurrentTime <= (Period * 0.5)) //Треугольные импульсы.
  {
    IntegratorTriangle = IntegratorTriangle + Ts;
  }
  else
  {
    IntegratorTriangle = IntegratorTriangle - Ts;
  }
  if (Period != 0.0)
  {
    Triangle = (((IntegratorTriangle * 2.0) / Period) * Amplitude) + Offset;
  }

  SummatorRnd = SummatorRnd * 1103515245 + 12345;
  //принудительно отбрасывающей младшие 16 и один старший разряд.
  uint32_t Tmp;
  Tmp = SummatorRnd & 0b01111111111111110000000000000000;
  //Арифметический сдвиг вправо на 16бит.
  Tmp = Tmp >> 16;
  //Масштабирование 0...32767 -> 0...1
  Prnd = ( ((float)Tmp) / 32767.0 ) * Amplitude + Offset;

  CurrentTime = CurrentTime + Ts; //Формирование периода.
  if (CurrentTime >= Period)
  {
    CurrentTime = 0.0;
    IntegratorTriangle = 0.0;
  }

  //Выходные переменные, сохраняемые.
  p->Sine = Sine;
  p->Cosine = Cosine;
  p->RectangleR = RectangleR;
  p->RectangleB = RectangleB;
  p->Triangle = Triangle;
  p->Prnd = Prnd;
  //Внутренние переменные, сохраняемые.
  p->CurrentTime = CurrentTime;
  p->IntegratorTriangle = IntegratorTriangle;
  p->SummatorRnd = SummatorRnd;

  return;
}
