import RPi.GPIO as GPIO
from SimpleMFRC522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
	print("Place Your Card")
	id, text = reader.read()
	print(id)
	print(text)

finally:
	GPIO.cleanup()
