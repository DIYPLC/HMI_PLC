#ifdef __cplusplus
extern "C"
{
#endif

bool Read_bool(void);
uint8_t Read_uint8_t(void);
uint16_t Read_uint16_t(void);
uint32_t Read_uint32_t(void);
uint64_t Read_uint64_t(void);
int8_t Read_int8_t(void);
int16_t Read_int16_t(void);
int32_t Read_int32_t(void);
int64_t Read_int64_t(void);
float Read_float(void);
double Read_double(void);

void Write_bool(bool in);
void Write_uint8_t(uint8_t in);
void Write_uint16_t(uint16_t in);
void Write_uint32_t(uint32_t in);
void Write_uint64_t(uint64_t in);
void Write_int8_t(int8_t in);
void Write_int16_t(int16_t in);
void Write_int32_t(int32_t in);
void Write_int64_t(int64_t in);
void Write_float(float in);
void Write_double(double in);

#ifdef __cplusplus
}
#endif
