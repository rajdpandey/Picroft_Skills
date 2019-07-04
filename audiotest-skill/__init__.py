from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.messagebus.message import Message
from mycroft.util import play_mp3


class Test(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

        # def initialize(self):
        #     try:
        #         # pin 23 is the GPIO pin the button is attached to
        #         # pin 25 is the GPIO pin the LED light is attached to
        #         GPIO.setmode(GPIO.BOARD)
        #         GPIO.setwarnings(False)
        #         #GPIO.setup(15, GPIO.OUT)
        #         #GPIO.setup(11, GPIO.OUT)
        #         pass
        #     except GPIO.error:
        #         self.log.warning("Cant initialize GPIO - skill will not load")
        #         self.speak_dialog("error.initialise")
        #     # finally:
        #         # self.add_event('recognizer_loop:record_begin',
        #                        # self.handle_listener_started)
        #         # self.add_event('recognizer_loop:record_end',
        #                        # self.handle_listener_ended)

    def play_first_file(self):
        play_process = play_mp3(self.root_dir + '/speech.mp3')

    def play_second_file(self):
        play_process = play_mp3("speech1.mp3")

    @intent_handler(IntentBuilder("").require("test"))
    def handle_listener_started(self):
        # code to excecute when active listening begins...
        self.play_first_file()

    @intent_handler(IntentBuilder("").require("test1"))
    def handle_listener_ended(self):
        self.play_second_file()


def create_skill():
    return Test()
