//Фильтр апериодический.
//      DbFilterA
//    +-----------+
//    | FbFilterA |
// ->-|In      Out|->-
//   -|Tf         |
//   -|Ts         |
//    +-----------+

#ifdef __cplusplus
extern "C"
{
#endif

struct DbFilterA
{
  //Входные переменные, сохраняемые.
  float In; //Входной сигнал до фильтрации.
  float Tf; //Постоянная времени фильтра [с].
  float Ts; //Шаг дискретизации по времени [с].
  //Выходные переменные, сохраняемые.
  float Out; //Выходной сигнал после фильтрации.
};

void FbFilterA(struct DbFilterA *p);

#ifdef __cplusplus
}
#endif

//static struct DbFilterA DbFilterA1;
//DbFilterA1.In = 0.0;            //Входной сигнал до фильтрации.
//DbFilterA1.Tf = 1.0;            //Постоянная времени фильтра [с].
//DbFilterA1.Ts = 0.1;            //Шаг дискретизации по времени [с].
//FbFilterA(&DbFilterA1);         //
//              = DbFilterA1.Out; //Выходной сигнал после фильтрации.

