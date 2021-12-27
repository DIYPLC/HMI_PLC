import time

#Real time
def Task1(Reset = False, Ts_ns = 0):
    global Timer1
    Ts = float(Ts_ns) / 1000000000.0 #[s]
    Timer1 = Timer1 + Ts
    time.sleep(1) #DEBUG BIG DELAY!
    print(int(Timer1))
    return 0

Timer1 = 0.0 #[s]
Unix_time_ns  = time.time_ns()
Unix_time_ns_previous = Unix_time_ns
Ts_ns = 0
Task1(Reset = True, Ts_ns = 0)

while True:
    Unix_time_ns = time.time_ns()
    Ts_ns = Unix_time_ns - Unix_time_ns_previous
    Unix_time_ns_previous = Unix_time_ns
    Task1(Reset = False, Ts_ns = Ts_ns)

