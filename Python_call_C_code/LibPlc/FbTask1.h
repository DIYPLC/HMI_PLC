//Задача для вызова программ №1.
//      DbTask1
//    +---------+
//    | FbTask1 |
// ->-|Ts_ms    |
// ->-|Reset    |
//    +---------+

#ifdef __cplusplus
extern "C"
{
#endif

struct DbTask1
{
uint32_t Ts_ms; //Шаг дискретизации по времени [мс].
bool     Reset; //Сброс при перезагрузке.
};

void FbTask1(struct DbTask1 *p);

#ifdef __cplusplus
}
#endif

//static struct DbTask1 DbTask_1;
//DbTask_1.Ts_ms = 100  ; //Шаг дискретизации по времени [мс].
//DbTask_1.Reset = false; //Сброс при перезагрузке.
//FbTask1(&DbTask_1)    ; //Задача для вызова программ №1.
