#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO

BTN_1 = 16

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BTN_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    pressed = False

    while True:
        # button is pressed when pin is LOW
        if not GPIO.input(BTN_1):
            if not pressed:
                print("Button 1 pressed")
                pressed = True
            else:
                pressed = False;
            time.sleep(0.1)
