from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.messagebus.message import Message

import RPi.GPIO as GPIO
import time
import os
import sys
import serial 

ser = serial.Serial('/dev/ttyS0',9600)

class Test(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        try:
            # pin 23 is the GPIO pin the button is attached to
            # pin 25 is the GPIO pin the LED light is attached to
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            #GPIO.setup(15, GPIO.OUT)
            #GPIO.setup(11, GPIO.OUT)
            pass
        except GPIO.error:
            self.log.warning("Cant initialize GPIO - skill will not load")
            self.speak_dialog("error.initialise")
        # finally:
            # self.add_event('recognizer_loop:record_begin',
                           # self.handle_listener_started)
            # self.add_event('recognizer_loop:record_end',
                           # self.handle_listener_ended)
	@intent_handler(IntentBuilder("").require("on_tv"))
    def handle_listener_started(self):
        # code to excecute when active listening begins...
        ser.write("a".encode()) # Writing In Console O by encoding
        time.sleep(0.2) # matching Delay time with arduino
        e = ser.readline() #Reading Console of Arduino 
		
	@intent_handler(IntentBuilder("").require("off_tv"))
    def handle_listener_ended(self):
        ser.write("b".encode()) # Writing In Console O by encoding
		#print(len(data))
        time.sleep(0.2) # matching Delay time with arduino
        t = ser.readline() #Reading Console of Arduino 


def create_skill():
    return Test()
