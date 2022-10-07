#!/usr/bin/env python3

import signal
import time
import sys
import RPi.GPIO as GPIO
import pygame


# Interrupt inputs

thumb_btns = [2,3,4,5]
fingr_btns = [6,7,8,9]

BTN_2 = 20
BOUNCE = 100

playlist = 0

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

def btn_pressed_callback(channel):
    global playlist

    playlist = channel;

    
def btn_1_pressed_callback(channel):
    global playlist

    playlist=1
    print("call 1 " + str(channel))

def btn_2_pressed_callback(channel):
    global playlist

    playlist=2
    print("call 2 " + str(channel))



if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)

    for btn in thumb_btns:
        GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(btn, GPIO.FALLING, callback=btn_pressed_callback, bouncetime=BOUNCE)

    signal.signal(signal.SIGINT, signal_handler)

    pygame.mixer.init()

    while True:
        if (playlist == 2):
            print("Button 2 pressed")
            sound = pygame.mixer.Sound('/home/icydee/Documents/drama/data/ding.wav')
            playing = sound.play()
            while playing.get_busy():
                pygame.time.delay(100)
            if playlist == 2:
                playlist = 0
        if (playlist == 3):
            print("Button 3 pressed")
            sound = pygame.mixer.Sound('/home/icydee/Documents/drama/data/comic.wav')
            playing = sound.play()
            while playing.get_busy():
                pygame.time.delay(100)
            if playlist == 3:
                playlist = 0
        if (playlist == 4):
            print("Button 4 pressed")
            sound = pygame.mixer.Sound('/home/icydee/Documents/drama/data/horn.wav')
            playing = sound.play()
            while playing.get_busy():
                pygame.time.delay(100)
            if playlist == 4:
                playlist = 0
        if (playlist == 5):
            print("Button 5 pressed")
            sound = pygame.mixer.Sound('/home/icydee/Documents/drama/data/sparkle.wav')
            playing = sound.play()
            while playing.get_busy():
                pygame.time.delay(100)
            if playlist == 5:
                playlist = 0
        
        time.sleep(0.1)


