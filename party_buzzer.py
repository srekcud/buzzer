#!/usr/bin/env python3
from BuzzController import BuzzController
import time
from threading import Thread 

_CLEANING_TIME = 10
buzz = BuzzController()
t1=""
t2=""

while True:

    t1=Thread(target=buzz.light_blinking)
    print("Ready -- start blink")
    t1.start()
    print("wait button")
    buzzPressed = buzz.get_first_red_pressed()
    print(buzzPressed+1)
    buzz.blink_status = False
    t1.join()

    buzz.light(buzzPressed)

    t2=Thread(target=buzz.clean_read)
    print("start clean")
    t2.start()
    time.sleep(_CLEANING_TIME) # avoid multiple answers due to spam buttons
    buzz.clean_status = False
    t2.join()

