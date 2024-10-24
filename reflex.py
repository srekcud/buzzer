#!/usr/bin/env python3

from random import randrange
from BuzzController import BuzzController
from threading import Thread 
import time



_MAX_WAITING_TIME = 3

buzz = BuzzController()
while True:
    lighted = randrange(4) 
    print("allume le : " + str(lighted))
    buzz.light(lighted)
    print("wait button")
    buzz.get_good_red_pressed(lighted)
    print("good")
    buzz.noLight()
    time.sleep(randrange(_MAX_WAITING_TIME))
