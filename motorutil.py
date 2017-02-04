#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import math
import threading

GPIO.setmode(GPIO.BOARD)

INTERVAL = 0.002
OUTPUTS = [
    [GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.LOW],
    [GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW],
    [GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.HIGH],
    [GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH]
]


class Motor:
    def __init__(self, steps, pins, id):
        self.steps = steps  # 何ステップで1回転であるか
        self.pins = pins  # ピンアサイン
        self.state = 0  # stateの初期化
        for pin in pins:
            GPIO.setup(pin, GPIO.OUT)  # 各ピンをOUTPUT用にセットアップ

    def add_state(self, num):
        u"""stateにステップ数を加算する"""
        self.state += num
        self.state %= self.steps

    def move_4steps(self, direction=1, interval=INTERVAL):
        u"""モータを4ステップ動かす"""
        for o in OUTPUTS[::direction]:
            # 4-sou 1
            GPIO.output(self.pins[0], o[0])
            GPIO.output(self.pins[1], o[1])
            GPIO.output(self.pins[2], o[2])
            GPIO.output(self.pins[3], o[3])
            print o
            print self.pins
            self.add_state(direction)
            self.printe_state()
            time.sleep(interval)

    def move_steps(self, num_steps, speed=1.0):
        u"""モータを指定されたステップ数分だけ動かす"""
        interval = INTERVAL * speed
        abs_num_steps = abs(num_steps)
        direction = int(math.copysign(1, num_steps))
        num_loop = int(abs_num_steps / 4)
        for i in range(num_loop):
            self.move_4steps(direction=direction)

    def move_degree(self, degree, speed=1.0):
        u"""モータを指定された角度だけ動かす"""
        # (1周のステップ数/360度) * 何度回したいか = 必要なステップ数
        # 必要なステップ数 / 4 = 必要なループ数
        num_steps = int((self.steps / 360.0) * degree)
        self.move_steps(num_steps, speed)

    def reset(self):
        u"""モーターを初期位置にリセットする"""
        # 1周のステップ数 - 現在ステップ数 = 足りないステップ数
        # 現在ステップ数0の場合があるので、1周のステップ数の剰余を取る
        rest_steps = (self.steps - self.state) % self.steps
        self.move_steps(rest_steps)

    def printe_state(self):
        u"""モーターの現在のステップ数を表示する"""
        print self.state


motors = [
    Motor(200, [31, 35, 33, 37], id="0"),
    Motor(200, [32, 38, 36, 40], id="1"),
    Motor(400, [8, 12, 10, 16], id="2"),
    Motor(400, [18, 24, 22, 26], id="3"),
    Motor(400, [7, 13, 11, 15], id="4"),
]

if __name__ == '__main__':
    # 使い方の例
    def move_motor1():
        u"""motor1をいい感じに動かす"""
        motor = motors[1]  # 1個選ぶ
        motor.move_degree(90)  # 90度回転
        time.sleep(1)  # 1秒停止
        motor.move_degree(45)  # 45度回転
        time.sleep(1)  # 1秒停止
        motor.move_degree(-45)  # 45度戻す
        time.sleep(1)  # 1秒停止
        motor.reset()  # リセット = 360 - 90 - 45 = 225 度回転


    def move_motor3():
        u"""motor3をいい感じに動かす"""
        motor = motors[3]  # 1個選ぶ
        motor.move_degree(180)  # 180度回転
        motor.move_degree(-180, speed=0.5)  # 180度戻す
        time.sleep(1)  # 1秒停止
        motor.move_degree(45)  # 45度首振りを3回
        motor.move_degree(-45)  # 45度首振りを3回
        motor.move_degree(45)  # 45度首振りを3回
        motor.move_degree(-45)  # 45度首振りを3回
        motor.move_degree(45)  # 45度首振りを3回
        motor.move_degree(-45)  # 45度首振りを3回
        time.sleep(1)  # 1秒停止
        motor.reset()  # リセット

    try:
        t1 = threading.Timer(0, move_motor1)
        t2 = threading.Timer(0, move_motor3)
        t1.start()
        t2.start()
    finally:
        for motor in motors:
            motor.reset()