#!/usr/bin/env python3

from random import randrange
from BuzzController import BuzzController
from threading import Thread 
import time



_MAX_WAITING_TIME = 3
_MAX_TIME = 120

_TIMEOUT = time.time() + _MAX_TIME
score = 0

buzz = BuzzController()
while True:
    if time.time() > _TIMEOUT:
        break
    lighted = randrange(4) 
    print("allume le : " + str(lighted))
    buzz.light(lighted)
    print("wait button")
    buzz.get_good_red_pressed(lighted)
    print("good")
    buzz.noLight()
    score+= 1
    time.sleep(randrange(_MAX_WAITING_TIME))

print("End of process")
print("Score : " + str(score))