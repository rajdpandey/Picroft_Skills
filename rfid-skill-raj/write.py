import RPi.GPIO as GPIO
from SimpleMFRC522 import SimpleMFRC522

reader =  SimpleMFRC522()

try:
	text = input('New Data :')
	print("Now Place Your Tag to Write")
	reader.write(text)
	print("Written")

finally:
	GPIO.cleanup()