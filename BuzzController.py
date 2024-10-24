#!/usr/bin/env python3

import hid
import time
from threading import Thread


class BuzzController:
    blink_status = False
    clean_status = False

    light_all = [0x00, 0x00, 0xFF, 0xFF, 0xFF, 0xFF, 0x00, 0x00]
    light_on = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    light_off = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

    buttonState = [
        {"red": False, "blue": False, "orange": False, "green": False, "yellow": False},
        {"red": False, "blue": False, "orange": False, "green": False, "yellow": False},
        {"red": False, "blue": False, "orange": False, "green": False, "yellow": False},
        {"red": False, "blue": False, "orange": False, "green": False, "yellow": False}
    ]
    def __init__(self):
        self.hid = hid.device()
        self.hid.open(0x054C,0x0002)
        self.hid.set_nonblocking(1)
        self.hid.write(self.light_off)
    

    def light_blinking(self,_SLEEP_TIME=0.5):
        if (not self.blink_status):
            self.blink_status = True
        while self.blink_status:
            self.hid.write(self.light_all)
            time.sleep(_SLEEP_TIME)
            self.hid.write(self.light_off)
            time.sleep(_SLEEP_TIME)

    def noLight(self):
        self.hid.write(self.light_off)

    def light(self,id):
        self.light_on = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        self.light_on[id + 2] = 0xFF
        self.hid.write(self.light_on)

    def get_red_status(self):
        data = self.hid.read(5)

        if data:
            self.buttonState[0]["red"] = ((data[2] & 0x01) != 0) #RED1
            self.buttonState[1]["red"] = ((data[2] & 0x20) != 0) #RED2
            self.buttonState[2]["red"] = ((data[3] & 0x04) != 0) #RED3
            self.buttonState[3]["red"] = ((data[3] & 0x80) != 0) #RED4
        return self.buttonState
    
    def get_color_status(self):
        data = self.hid.read(5)

        if data:
            self.buttonState[0]["yellow"] = ((data[2] & 0x02) != 0) #yellow
            self.buttonState[0]["green"] = ((data[2] & 0x04) != 0) #green
            self.buttonState[0]["orange"] = ((data[2] & 0x08) != 0) #orange
            self.buttonState[0]["blue"] = ((data[2] & 0x10) != 0) #blue

            self.buttonState[1]["yellow"] = ((data[2] & 0x40) != 0) #yellow
            self.buttonState[1]["green"] = ((data[2] & 0x80) != 0) #green
            self.buttonState[1]["orange"] = ((data[3] & 0x01) != 0) #orange
            self.buttonState[1]["blue"] = ((data[3] & 0x02) != 0) #blue

            self.buttonState[2]["yellow"] = ((data[3] & 0x08) != 0) #yellow
            self.buttonState[2]["green"] = ((data[3] & 0x10) != 0) #green
            self.buttonState[2]["orange"] = ((data[3] & 0x20) != 0) #orange
            self.buttonState[2]["blue"] = ((data[3] & 0x40) != 0) #blue

            self.buttonState[3]["yellow"] = ((data[4] & 0x01) != 0) #yellow
            self.buttonState[3]["green"] = ((data[4] & 0x02) != 0) #green
            self.buttonState[3]["orange"] = ((data[4] & 0x04) != 0) #orange
            self.buttonState[3]["blue"] = ((data[4] & 0x08) != 0) #blue
        return self.buttonState

    
    def get_first_red_pressed(self):
        while True:
            buttons = self.get_red_status()
            for i in range(4):
                if (buttons[i]["red"]):
                    return i
    
    def get_good_red_pressed(self,id):
        while True:
            buttons = self.get_red_status()
            if (buttons[id]["red"]):
                self.clean()
                return 1
    
    def get_first_color_pressed(self):
        while True:
            buttons = self.get_color_status()
            for i in range(4):
                if (buttons[i]["blue"]):
                    return "blue"
                elif (buttons[i]["orange"]):
                    return "orange"
                elif (buttons[i]["yellow"]):
                    return "yellow"
                
    def clean_read(self):
        self.clean()
        if (not self.clean_status):
            self.clean_status = True
        while self.clean_status:
            data = self.hid.read(5)
        
    def clean(self):
        self.buttonState = [
        {"red": False, "blue": False, "orange": False, "green": False, "yellow": False},
        {"red": False, "blue": False, "orange": False, "green": False, "yellow": False},
        {"red": False, "blue": False, "orange": False, "green": False, "yellow": False},
        {"red": False, "blue": False, "orange": False, "green": False, "yellow": False}
        ]
        
        