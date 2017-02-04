#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(31, GPIO.OUT) # GPIO 6 
GPIO.setup(33, GPIO.OUT) # GPIO 13 
GPIO.setup(35, GPIO.OUT) # GPIO 19 
GPIO.setup(37, GPIO.OUT) # GPIO 26 

INTERVAL = 0.002

OUTPUTS = [
    [ GPIO.HIGH, GPIO.HIGH, GPIO.LOW,  GPIO.LOW  ],
    [ GPIO.LOW,  GPIO.HIGH, GPIO.HIGH, GPIO.LOW  ],
    [ GPIO.LOW,  GPIO.LOW,  GPIO.HIGH, GPIO.HIGH ],
    [ GPIO.HIGH, GPIO.LOW,  GPIO.LOW,  GPIO.HIGH ]
]

for i in range(200):
    print i
    for o in OUTPUTS[::-1]:
        GPIO.output(31, o[0])
        GPIO.output(35, o[1])
        GPIO.output(33, o[2])
        GPIO.output(37, o[3])
        time.sleep(INTERVAL)
