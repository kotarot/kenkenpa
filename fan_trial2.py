#!/usr/bin/python
# -*- coding: utf-8 -*-

from motorutil import *

if __name__ == '__main__':
    motor = motors[3]
    for i in range(10):
        motor.move_degree(60, speed=0.5)
        time.sleep(2)
        motor.move_degree(-60, speed=0.5)
        time.sleep(2)
        #time.sleep(0.01)

