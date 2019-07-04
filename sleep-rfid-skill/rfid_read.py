#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
from .MFRC522 import MFRC522
import signal

continue_reading = True


class Read(object):
    """docstring for ClassName"""

    def __init__(self):
        self.rfidscanner()

    # Capture SIGINT for cleanup when the script is aborted
    def end_read(signal, frame):
        global continue_reading
        print("Ctrl+C captured, ending read.")
        continue_reading = False
        GPIO.cleanup()

    def rfidscanner(self):
        print("inside rfidscanner")
        global user
        # Hook the SIGINT
        # signal.signal(signal.SIGINT, end_read)

        # Create an object of the class MFRC522
        MIFAREReader = MFRC522()
        # This loop keeps checking for chips. If one is near it will get the UID and authenticate
        while continue_reading:

            # Scan for cards
            (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

            # If a card is found
            if status == MIFAREReader.MI_OK:
                print("Card detected")
            if status != MIFAREReader.MI_OK:
                print("Not Detected")
            # Get the UID of the card
            (status, uid) = MIFAREReader.MFRC522_Anticoll()

            # If we have the UID, continue
            if status == MIFAREReader.MI_OK:

                # Print UID
                print("Card read UID: " + str(uid[0]) + "," + str(uid[1]) + "," + str(uid[2]) + "," + str(
                    uid[3]) + "," + str(uid[4]))

                # This is the default key for authentication
                key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

                # Select the scanned tag
                MIFAREReader.MFRC522_SelectTag(uid)

                # Authenticate
                status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)
                user1 = uid
                user = str(user1)
                print(user)
                if uid != "":
                    MIFAREReader.Close_MFRC522()
                    break
                # Check if authenticated
                if status == MIFAREReader.MI_OK:
                    MIFAREReader.MFRC522_Read(8)
                    MIFAREReader.MFRC522_StopCrypto1()
                else:
                    print("Authentication error")
                return user
            else:
                user = "goodbye"
                MIFAREReader.Close_MFRC522()
                return user

    def userid(self):

        print("This is User : " + str(user))
        if user == "[82, 19, 245, 28, 168]":
            eric = "Eric"
            return eric
        elif user == "[218, 190, 138, 171, 69]":
            raj = "Raj"
            return raj
        elif user == "[6, 92, 136, 161, 115]":
            james = "James"
            return james
        elif user == "goodbye":
            hey = "bye"
            return hey
