import time

def Write_to_Error_file(text = "text"):
    #Записываем ошибки в файл если файл слишком большой стираем его и пишем в чистый файл.
    _FILE_NAME = "Error.txt"
    _MAX_FILE_SIZE_BYTES = 4096
    _TEXT = str(time.strftime("%d-%b-%Y %H:%M:%S")) + ' ' + str(text) + '\n'
    try: #Получить размер файла в байтах.
        File_size_butes = os.path.getsize(_FILE_NAME)
    except: #если нет такого файла то размер его 0.
        File_size_butes = 0
    if (File_size_butes < _MAX_FILE_SIZE_BYTES): #Ограничим размер файла.
        f = open(_FILE_NAME, 'a') #Дописать текст в файл если нет создать.
    else:
        f = open(_FILE_NAME, 'w') #Записать в пустой файл.
    print(_TEXT)
    f.write(_TEXT)
    f.close()
    return

def Unit_test():
    Write_to_Error_file("Unit test for error file")
    return

if (__name__ == "__main__"):
    Unit_test()
    input("press any key for exit...")
