#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Copyright 2014,2018 Mario Gomez <mario.gomez@teubi.co>
#
#    This file is part of MFRC522-Python
#    MFRC522-Python is a simple Python implementation for
#    the MFRC522 NFC Card Reader for the Raspberry Pi.
#
#    MFRC522-Python is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    MFRC522-Python is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with MFRC522-Python.  If not, see <http://www.gnu.org/licenses/>.
#

import RPi.GPIO as GPIO
from .MFRC522 import MFRC522
#import signal

continue_reading = True


def ___init__():
    continue_read()


# Capture SIGINT for cleanup when the script is aborted
# def end_read(signal, frame):
#     global continue_reading
#     print("Ctrl+C captured, ending read.")
#     continue_reading = False
#     GPIO.cleanup()


# Hook the SIGINT
#signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522()


# Welcome message
def continue_read():
    # This loop keeps checking for chips. If one is near it will get the UID and authenticate
    while continue_reading:
        print("Card Found")
        # Scan for cards
        (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

        # If a card is found
        if status == MIFAREReader.MI_OK:
            print("Card detected")

        # Get the UID of the card
        (status, uid) = MIFAREReader.MFRC522_Anticoll()

        # If we have the UID, continue
        if status == MIFAREReader.MI_OK:

            # Print UID
            print("Card read UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3]))
            print(type(uid))
            # This is the default key for authentication
            key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

            # Select the scanned tag
            MIFAREReader.MFRC522_SelectTag(uid)

            # Authenticate
            status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

            # Check if authenticated
            if status == MIFAREReader.MI_OK:
                MIFAREReader.MFRC522_Read(8)
                MIFAREReader.MFRC522_StopCrypto1()
            else:
                print("Authentication error")
        print("Card UID : " + str(uid))
        return uid


def user():
    uid = continue_read()
    print(uid)
    print("Card : " + str(type(uid)))
    if uid == [82, 19, 245, 28, 168]:
        return "Eric"
    elif uid == [218, 190, 138, 171, 69]:
        return "Raj"
    elif uid == [6, 92, 136, 161, 115]:
        return "James"
    else:
        return ""

