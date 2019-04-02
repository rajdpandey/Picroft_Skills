from mycroft import MycroftSkill
import RPi.GPIO as GPIO
# from .SimpleMFRC522 import SimpleMFRC522
from threading import Thread
from .read import user
import time

reader = user()
RED = 11
GREEN = 15
GPIO.setwarnings(False)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)


class Rfid(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.stopped = False
        self.status = False
        self.thread = Thread(target=self.read_thread)
        self.thread.daemon = True
        self.thread.start()
        self.stop = True
        self.stop1 = False
        self.read = False

    def read_thread(self):
        while not self.stopped:
            if reader != "":
                if self.stop == True:
                    self.confirm()
                    self.stop = False
                # self.id, self.text = reader.read_no_block()
                # while self.text is not None:
                #     if self.stop == True:
                #         self.confirm()
                #         self.stop = False
                # if self.text is None:
                #     if self.stop1 ==false:
                #         self.unconfirm()
                #         self.stop1 = True

    def confirm(self):
        GPIO.output(GREEN, GPIO.HIGH)
        GPIO.output(RED, GPIO.LOW)
        response = {'text': self.text}
        self.speak_dialog("to.hello.say", data=response)
        time.sleep(5)
        GPIO.output(GREEN, GPIO.LOW)
        GPIO.output(RED, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(RED, GPIO.LOW)
        GPIO.output(GREEN, GPIO.LOW)

    def unconfirm(self):
        GPIO.output(RED, GPIO.HIGH)
        GPIO.output(GREEN, GPIO.LOW)
        self.speak_dialog("to.bye.say")
        time.sleep(2)

    def shutdown(self):
        self.stopped = True


def create_skill():
    return Rfid()
