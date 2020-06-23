import time, threading
from threading import Thread

SECS = 60
t = 100 * SECS
def countdown(): 
    global t
    while t >= 0: 
        mins, secs = divmod(t, 6000) 
        secs, mill = divmod(t, 100)
        timeformat = '{:1d}:{:02d}.{:02d}'.format(mins, secs, mill) 
        print(timeformat, end='\r') 
        time.sleep(0.01) 
        t -= 1
    print()
    t = 100 * SECS
    countdown()

reset = False
countdown_thread = Thread(target=countdown, daemon=True)
countdown_thread.start()
while True:
    t = 100 * SECS
    input()
