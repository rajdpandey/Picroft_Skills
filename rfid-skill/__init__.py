from mycroft import MycroftSkill
import RPi.GPIO as GPIO
from threading import Thread
from multiprocessing import Pool
from .rfid_read import Read
import time
from .MFRC522 import MFRC522

RED = 11
GREEN = 15
GPIO.setwarnings(False)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.output(RED, GPIO.LOW)
GPIO.output(GREEN, GPIO.LOW)


class Rfid(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        counter = 0
        self.stopped = False
        self.status = False
        game = "Thread" + str(counter)
        self.thread = Thread(target=self.read_thread, name=game)
        counter += 1
        self.thread.daemon = True
        self.thread.start()
        self.stop = True
        self.stop1 = True

    def read_thread(self):
        while not self.stopped:
            print(self.thread.name)
            name = Read()
            user = name.userid()
            if user != "bye":
                if user == "Raj" or user == "Eric" or user == "James":
                    if self.stop == True:
                        GPIO.output(GREEN, GPIO.HIGH)
                        GPIO.output(RED, GPIO.LOW)
                        response = {'text': user}
                        self.speak_dialog("to.hello.say", data=response)
                        time.sleep(1)
                        GPIO.output(GREEN, GPIO.LOW)
                        GPIO.output(RED, GPIO.HIGH)
                        time.sleep(1)
                        GPIO.output(RED, GPIO.LOW)
                        GPIO.output(GREEN, GPIO.LOW)
                        self.stop = False
                        self.stop1 = False

            else:
                if self.stop1 == False:
                    GPIO.output(RED, GPIO.HIGH)
                    GPIO.output(GREEN, GPIO.LOW)
                    self.speak_dialog("to.bye.say")
                    time.sleep(2)
                    GPIO.output(RED, GPIO.LOW)
                    GPIO.output(GREEN, GPIO.LOW)
                    self.stop = True
                    self.stop1 = True

    def shutdown(self):
        self.stopped = True


def create_skill():
    return Rfid()
