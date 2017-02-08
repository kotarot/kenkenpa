#!/usr/bin/python
# -*- coding: utf-8 -*-

from motorutil import *

if __name__ == '__main__':
    motor = motors[0]
    motor.move_degree(360)  # 90度回転
    time.sleep(0.1)  # 1秒停止
    motor.move_degree(-360)  # 90度回転
    time.sleep(0.1)  # 1秒停止
    motor.move_degree(360)  # 90度回転
    time.sleep(0.1)  # 1秒停止
    motor.move_degree(-360)  # 90度回転
    # def move_motor1():
    #     u"""motor1をいい感じに動かす"""
    #     motor = motors[1]  # 1個選ぶ
    #     motor.move_degree(90)  # 90度回転
    #     time.sleep(1)  # 1秒停止
    #     motor.move_degree(45)  # 45度回転
    #     time.sleep(1)  # 1秒停止
    #     motor.move_degree(-45)  # 45度戻す
    #     time.sleep(1)  # 1秒停止
    #     motor.reset()  # リセット = 360 - 90 - 45 = 225 度回転
    #
    #
    # def move_motor3():
    #     u"""motor3をいい感じに動かす"""
    #     motor = motors[3]  # 1個選ぶ
    #     motor.move_degree(180)  # 180度回転
    #     motor.move_degree(-180, speed=0.5)  # 180度戻す
    #     time.sleep(1)  # 1秒停止
    #     motor.move_degree(45)  # 45度首振りを3回
    #     motor.move_degree(-45)  # 45度首振りを3回
    #     motor.move_degree(45)  # 45度首振りを3回
    #     motor.move_degree(-45)  # 45度首振りを3回
    #     motor.move_degree(45)  # 45度首振りを3回
    #     motor.move_degree(-45)  # 45度首振りを3回
    #     time.sleep(1)  # 1秒停止
    #     motor.reset()  # リセット
    #
    # try:
    #     t1 = threading.Timer(0, move_motor1)
    #     t2 = threading.Timer(0, move_motor3)
    #     t1.start()
    #     t2.start()
    # finally:
    #     for motor in motors:
    #         motor.reset()