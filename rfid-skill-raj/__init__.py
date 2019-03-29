from mycroft import MycroftSkill
import RPi.GPIO as GPIO
from .SimpleMFRC522 import SimpleMFRC522
from threading import Thread
import time

reader = SimpleMFRC522()
RED = 11
GREEN = 15
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(RED,GPIO.OUT)
GPIO.setup(GREEN,GPIO.OUT)

class Rfid(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.stopped = False
        self.thread = Thread(target=self.read_thread)
        self.thread.daemon = True
        self.thread.start()
		
    def read_thread(self):
        while not self.stopped:
            self.id, self.text = reader.read_no_block()
            if self.text is not None:
              #  GPIO.output(GREEN,GPIO.HIGH)
              #  GPIO.output(RED,GPIO.LOW)
              #  response = {'text': self.text}
              #  self.speak_dialog("to.hello.say", data=response)
              #  time.sleep(10)
              #  GPIO.cleanup()
                self.confirm()
            elif self.text is None:
              #  self.speak_dialog("to.bye.say")
              #  GPIO.output(RED,GPIO.HIGH)
              #  GPIO.output(GREEN,GPIO.LOW)
                self.unconfirm()
    def confirm(self):
        GPIO.output(GREEN,GPIO.HIGH)
        GPIO.output(RED,GPIO.LOW)
        response = {'text': self.text}
        self.speak_dialog("to.hello.say", data=response)
        time.sleep(2)
        GPIO.cleanup()
        return
    def unconfirm(self):
        GPIO.output(RED,GPIO.HIGH)
        GPIO.output(GREEN,GPIO.LOW)
        self.speak_dialog("to.bye.say")
        time.sleep(2)
        GPIO.cleanup()
        return
    def shutdown(self):
        self.stopped = True

def create_skill():
    return Rfid()
