#!/usr/bin/env python3

import signal
import time
import sys
import RPi.GPIO as GPIO
import pygame


# Interrupt inputs

thumb_btns = [2,3,4,5]
audio_btns = [6,7,8,9]

files = [
        [9,5,'ting.wav'], [9,4,'pong.wav'],        [9,3,'tinkle.wav'],  [9,2,'btfail.wav'],
        [8,5,'ting.wav'], [8,4,'p_up.wav'],        [8,3,'p_down.wav'],  [8,2,'beeps.wav'],
        [7,5,'ting.wav'], [7,4,'exterminate.wav'], [7,3,'mash.wav'],    [7,2,'claxon.wav'],
        [6,5,'ting.wav'], [6,4,'success.wav'],     [6,3,'failure.wav'], [6,2,'fart.wav']
        ]

BOUNCE = 100

playlist = 5
audio_bank = 9

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)


def btn_pressed_callback(channel):
    global playlist

    playlist = channel;

def bnk_pressed_callback(channel):
    global audio_bank

    audio_bank = channel;
    
if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)

    for bnk in audio_btns:
        GPIO.setup(bnk, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(bnk, GPIO.FALLING, callback=bnk_pressed_callback, bouncetime=BOUNCE)

    for btn in thumb_btns:
        GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(btn, GPIO.FALLING, callback=btn_pressed_callback, bouncetime=BOUNCE)

    signal.signal(signal.SIGINT, signal_handler)

    pygame.mixer.init()

    while True:

        for file in files:
            if (audio_bank == file[0] and playlist == file[1]):
                print("Button " + str(audio_bank) + "/" + str(playlist)+ " pressed [" + file[2] + "]")
                sound = pygame.mixer.Sound('/home/icydee/Documents/drama/data/' + file[2])
                playing = sound.play()
                while playing.get_busy():
                    pygame.time.delay(10)

                if (playlist == file[1]):
                    playlist = 0

        time.sleep(0.01)

