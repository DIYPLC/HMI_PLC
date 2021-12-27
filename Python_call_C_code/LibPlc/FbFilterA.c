#include "FbFilterA.h"

void FbFilterA(struct DbFilterA *p)
{
  //Внутренние переменные, не сохраняемые.
  float Tmp;
  //W(s) = 1/(1+Tf*s) при Ts->0.
  if (p->Tf <= 0.0)
  {
    p->Out = p->In;
  }
  else
  {
    Tmp = (p->In - p->Out) / p->Tf;
    p->Out = p->Out + Tmp * p->Ts;
  }
  return;
}
