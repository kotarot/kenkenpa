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

# 2-sou 1
GPIO.setup(8,  GPIO.OUT) # GPIO 14 
GPIO.setup(10, GPIO.OUT) # GPIO 15 
GPIO.setup(12, GPIO.OUT) # GPIO 18 
GPIO.setup(16, GPIO.OUT) # GPIO 23 

# 2-sou 2
GPIO.setup(18, GPIO.OUT) # GPIO 24 
GPIO.setup(22, GPIO.OUT) # GPIO 25 
GPIO.setup(24, GPIO.OUT) # GPIO 8 
GPIO.setup(26, GPIO.OUT) # GPIO 7 

# 2-sou 3
GPIO.setup(7,  GPIO.OUT) # GPIO 4 
GPIO.setup(11, GPIO.OUT) # GPIO 17 
GPIO.setup(13, GPIO.OUT) # GPIO 27 
GPIO.setup(15, GPIO.OUT) # GPIO 22 

INTERVAL = 0.002

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

        # 2-sou 1
        GPIO.output(8,  o[0])
        GPIO.output(12, o[1])
        GPIO.output(10, o[2])
        GPIO.output(16, o[3])

        # 2-sou 2
        GPIO.output(18, o[0])
        GPIO.output(24, o[1])
        GPIO.output(22, o[2])
        GPIO.output(26, o[3])

        # 2-sou 2
        GPIO.output(7,  o[0])
        GPIO.output(13, o[1])
        GPIO.output(11, o[2])
        GPIO.output(15, o[3])

        time.sleep(INTERVAL)
        print INTERVAL
