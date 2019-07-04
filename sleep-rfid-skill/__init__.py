from mycroft import MycroftSkill, intent_handler
from mycroft.messagebus.message import Message
from mycroft.audio import wait_while_speaking
from mycroft.configuration.config import Configuration
import RPi.GPIO as GPIO
from .rfid_read import Read
from .MFRC522 import MFRC522
import time

RED = 11
GREEN = 15
GPIO.setwarnings(False)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.output(RED, GPIO.LOW)
GPIO.output(GREEN, GPIO.LOW)


class RfidSleep(MycroftSkill):
    # def __init__(self):
    #     MycroftSkill.__init__(self)
    #     self.started_by_skill = True
    #     self.sleeping = True
    #     self.initialize()
    #     self.stopped = False
    #     self.thread = Thread(target=self.read_thread, name=game)
    #     self.thread.daemon = True
    #     self.thread.start()
    #     self.stop = True
    #     self.stop1 = True
    #     self.handle_go_to_sleep()

    def initialize(self):
        self.started_by_skill = True
        self.sleeping = True
        self.stopped = False
        self.handle_go_to_sleep()
        self.thread = Thread(target=self.read_thread)
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
                        self.handle_awoken()
                        response = {'text': user}
                        self.speak_dialog("to.hello.say", data=response)
                        wait_while_speaking()
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
                    wait_while_speaking()
                    time.sleep(2)
                    GPIO.output(RED, GPIO.LOW)
                    GPIO.output(GREEN, GPIO.LOW)
                    self.handle_go_to_sleep()
                    self.stop = True
                    self.stop1 = True

    def handle_go_to_sleep(self):
        print("In Sleep")
        self.sleeping = False
        self.started_by_skill = False
        if self.config_core.get("enclosure").get("platform", "unknown") != "unknown":
            self.bus.emit(Message('mycroft.volume.mute',
                                  data={"speak_message": False}))

    def handle_awoken(self):
        print("Awaked")
        if self.config_core.get("enclosure").get("platform", "unknown") != "unknown":
            self.bus.emit(Message('mycroft.volume.unmute',
                                  data={"speak_message": False}))
        self.sleeping = True
        self.started_by_skill = True

    def shutdown(self):
        self.stopped = True


def create_skill():
    return RfidSleep()
