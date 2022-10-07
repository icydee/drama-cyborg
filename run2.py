#!/usr/bin/env python3

import signal
import time
import sys
import RPi.GPIO as GPIO
import pygame

BTN_1 = 16
BTN_2 = 20
BOUNCE = 100

playlist = 0

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

def btn_1_pressed_callback(channel):
    global playlist
    playlist=1

def btn_2_pressed_callback(channel):
    global playlist
    playlist=2

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BTN_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BTN_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.add_event_detect(BTN_1, GPIO.FALLING,callback=btn_1_pressed_callback, bouncetime=BOUNCE)
    GPIO.add_event_detect(BTN_2, GPIO.FALLING,callback=btn_2_pressed_callback, bouncetime=BOUNCE)

    signal.signal(signal.SIGINT, signal_handler)

    pygame.mixer.init()

    while True:
        if (playlist == 1):
            print("Button 1 pressed")
            sound = pygame.mixer.Sound('/home/icydee/Documents/drama/data/fart03.wav')
            playing = sound.play()
            while playing.get_busy():
                pygame.time.delay(100)
            if playlist == 1:
                playlist = 0
        if (playlist == 2):
            print("Button 2 pressed")
            sound = pygame.mixer.Sound('/home/icydee/Documents/drama/data/fart04.wav')
            playing = sound.play()
            while playing.get_busy():
                pygame.time.delay(100)
            if playlist == 2:
                playlist = 0
        time.sleep(0.1)


