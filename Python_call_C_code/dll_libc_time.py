print("Example call function in DLL")
print("Test Windows 10 Python 3.11.2")
import ctypes
libc = ctypes.cdll.msvcrt
print(libc.time(None), "seconds")
input("press any key")
