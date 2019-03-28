from mycroft import MycroftSkill, intent_file_handler
import RPi.GPIO as GPIO
import SimpleMFRC522

class SayHelloTo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
		reader =  SimpleMFRC522.SimpleMFRC522()
		self.id, self.text = reader.read()
		
    #@intent_file_handler('to.hello.say.intent')
    def handle_say_hello_to_intent(self):
        response = {'text': self.text}
        self.speak_dialog("to.hello.say", data=response)


def create_skill():
    return SayHelloTo()
