from BuzzController import BuzzController
from threading import Thread 
import time


buzz = BuzzController()
_CLEANING_TIME = 2
_BLUE = "blue"
_ORANGE = "orange"
_YELLOW = "yellow"
t1=""
t2=""

while True:
    t1=Thread(target=buzz.light_blinking, args=(0.1,))
    print("start blinking menu")
    t1.start()
    print("wait color button press")
    buzzpressed = buzz.get_first_color_pressed()
    buzz.blink_status = False
    t1.join()
    print(buzzpressed)
    t2=Thread(target=buzz.clean_read)
    print("start clean")
    t2.start()
    time.sleep(_CLEANING_TIME) # avoid multiple answers due to spam buttons
    buzz.clean_status = False
    print("read clean")
    t2.join()
    if buzzpressed == _BLUE:
        import reflex 
    elif buzzpressed == _ORANGE:
        import beat_the_time
    elif buzzpressed == _YELLOW:
        import party_buzzer