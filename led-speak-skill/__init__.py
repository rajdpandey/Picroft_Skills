from mycroft import MycroftSkill
from mycroft.messagebus.message import Message

import time
import RPi.GPIO as GPIO


class James(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        try:
            # pin 23 is the GPIO pin the button is attached to
            # pin 25 is the GPIO pin the LED light is attached to
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(15, GPIO.OUT)
            GPIO.setup(11, GPIO.OUT)

            pass
        except GPIO.error:
            self.log.warning("Cant initialize GPIO - skill will not load")
            self.speak_dialog("error.initialise")
        finally:
            self.add_event('recognizer_loop:record_begin',
                           self.handle_listener_started)
            self.add_event('recognizer_loop:record_end',
                           self.handle_listener_ended)

    def handle_listener_started(self):
        # code to excecute when active listening begins...
        GPIO.output(15, GPIO.HIGH)
        GPIO.output(11, GPIO.LOW)

    def handle_listener_ended(self):
        GPIO.output(15, GPIO.LOW)
        GPIO.output(11, GPIO.LOW)



def create_skill():
    return James()
