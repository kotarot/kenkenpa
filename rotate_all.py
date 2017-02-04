#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# 4-sou 1
GPIO.setup(31, GPIO.OUT) # GPIO 6 
GPIO.setup(33, GPIO.OUT) # GPIO 13 
GPIO.setup(35, GPIO.OUT) # GPIO 19 
GPIO.setup(37, GPIO.OUT) # GPIO 26 

# 4-sou 2 
GPIO.setup(32, GPIO.OUT) # GPIO 12 
GPIO.setup(36, GPIO.OUT) # GPIO 16 
GPIO.setup(38, GPIO.OUT) # GPIO 20 
GPIO.setup(40, GPIO.OUT) # GPIO 21 

INTERVAL = 0.005

OUTPUTS = [
    [ GPIO.HIGH, GPIO.HIGH, GPIO.LOW,  GPIO.LOW  ],
    [ GPIO.LOW,  GPIO.HIGH, GPIO.HIGH, GPIO.LOW  ],
    [ GPIO.LOW,  GPIO.LOW,  GPIO.HIGH, GPIO.HIGH ],
    [ GPIO.HIGH, GPIO.LOW,  GPIO.LOW,  GPIO.HIGH ]
]

for i in range(10000):
    print i
    for o in OUTPUTS[::-1]:

        # 4-sou 1
        GPIO.output(31, o[0])
        GPIO.output(35, o[1])
        GPIO.output(33, o[2])
        GPIO.output(37, o[3])

        # 4-sou 1
        GPIO.output(32, o[0])
        GPIO.output(38, o[1])
        GPIO.output(36, o[2])
        GPIO.output(40, o[3])

        time.sleep(INTERVAL)
