#!/usr/bin/python
# -*- coding: utf-8 -*-
from recognition import *
from motorutil import *


def default_emotion(key):
    if len(key) % 2 == 0:
        return "positive"
    else:
        return "negative"


emotion_map = {
    "banana": "super_positive",
    "orange": "positive",
    "teddy": "positive",
    "laptop": "negative"
}


def label2emotion(label_en):
    u"""物体の英語ラベルを感情文字列に表現"""
    if label_en in emotion_map:
        emo = emotion_map[label_en]
    else:
        emo = default_emotion(label_en)
    return emo


def neutral_motor0():
    u"""羽モーターのニュートラル状態"""
    motor = motors[0]
    motor.reset()


def neutral_motor1():
    u"""尻尾モーターのニュートラル状態"""
    motor = motors[1]
    deg = 60
    motor.move_degree(deg, speed=0.5)
    time.sleep(1.5)
    motor.move_degree(-deg, speed=0.5)
    time.sleep(1.5)
    motor.reset()


def neutral_motor2():
    u"""首振りモーターのニュートラル状態"""
    motor = motors[2]
    motor.move_degree(30, speed=0.5)
    time.sleep(1.5)
    motor.move_degree(-30, speed=0.5)
    motor.reset()


def positive_motor0():
    u"""羽モーターのポジティブ感情状態"""
    motor = motors[0]
    motor.move_degree(360, speed=1)
    motor.reset()


def positive_motor1():
    u"""尻尾モーターのポジティブ感情状態"""
    motor = motors[1]
    deg = 60
    motor.move_degree(deg, speed=0.8)
    motor.move_degree(-deg, speed=0.8)
    motor.move_degree(deg, speed=0.8)
    motor.move_degree(-deg, speed=0.8)
    motor.reset()


def positive_motor2():
    u"""首振りモーターのポジティブ感情状態"""
    motor = motors[2]
    deg = 30
    motor.move_degree(deg, speed=0.5)
    motor.move_degree(-deg, speed=0.5)
    motor.reset()


def super_positive_motor0():
    u"""羽モーターの超ポジティブ感情状態"""
    motor = motors[0]
    motor.move_degree(360, speed=1)
    motor.reset()


def super_positive_motor1():
    u"""尻尾モーターの超ポジティブ感情状態"""
    motor = motors[3]
    deg = 90
    motor.move_degree(deg, speed=1)
    motor.move_degree(-deg, speed=1)
    motor.move_degree(deg, speed=1)
    motor.move_degree(-deg, speed=1)
    motor.move_degree(deg, speed=1)
    motor.move_degree(-deg, speed=1)
    motor.reset()


def super_positive_motor2():
    u"""首振りモーターの超ポジティブ感情状態"""
    motor = motors[2]
    deg = 30
    motor.move_degree(deg, speed=0.5)
    motor.move_degree(-deg, speed=0.5)
    motor.move_degree(deg, speed=0.5)
    motor.move_degree(-deg, speed=0.5)
    motor.move_degree(deg, speed=0.5)
    motor.move_degree(-deg, speed=0.5)
    motor.move_degree(deg, speed=0.5)
    motor.move_degree(-deg, speed=0.5)
    motor.reset()


def negative_motor0():
    u"""羽モーターのネガティブ感情状態"""
    motor = motors[0]
    motor.reset()


def negative_motor1():
    u"""尻尾モーターのネガティブ感情状態"""
    motor = motors[1]
    motor.reset()


def negative_motor2():
    u"""首振りモーターのネガティブ感情状態"""
    motor = motors[2]
    motor.move_degree(90, speed=1.0)
    time.sleep(3)
    motor.move_degree(-90, speed=1.0)
    motor.reset()


def reset_all_motors():
    u"""全モーターをゼロリセット"""
    for m in motors:
        m.reset()


def neutral_move():
    tm0 = threading.Timer(0, neutral_motor0)
    tm1 = threading.Timer(0, neutral_motor1)
    tm2 = threading.Timer(0, neutral_motor2)
    tm0.start()
    tm1.start()
    tm2.start()


def positive_move():
    u"""ポジティブのシーケンスを開始、5秒後に終了"""
    print "ポジティブ動作開始"
    tm0 = threading.Timer(0, positive_motor0)
    tm1 = threading.Timer(0, positive_motor1)
    tm2 = threading.Timer(0, positive_motor2)
    tm0.start()
    tm1.start()
    tm2.start()
    time.sleep(5)


def super_positive_move():
    u"""超ポジティブのシーケンスを開始、5秒後に終了"""
    print "超ポジティブ動作開始"
    tm0 = threading.Timer(0, super_positive_motor0)
    tm1 = threading.Timer(0, super_positive_motor1)
    tm2 = threading.Timer(0, super_positive_motor2)
    tm0.start()
    tm1.start()
    tm2.start()
    time.sleep(5)


def negative_move():
    u"""ネガティブのシーケンスを開始、5秒後に終了"""
    print "ネガティブ動作開始"
    tm0 = threading.Timer(0, negative_motor0)
    tm1 = threading.Timer(0, negative_motor1)
    tm2 = threading.Timer(0, negative_motor2)
    tm0.start()
    tm1.start()
    tm2.start()
    time.sleep(5)


if __name__ == '__main__':
    # ファンさんのデモを実行
    try:
        while True:
            # ニュートラル動作をバックグラウンドで実施 約3秒
            print "認識開始・ニュートラル動作開始"
            t_neutral = threading.Timer(0, neutral_move)
            t_neutral.start()

            # 認識実行 約3.6秒かかる
            (label_en, label_ja, prob) = recognize()

            if prob > 0.15:
                # 認識に成功した場合
                print(u"{} ({}) が見える (prob:{})".format(label_ja, label_en, prob))
                # 物体を認識したら一旦全モーターリセット
                reset_all_motors()

                # 物体から感情を判定
                emotion = label2emotion(label_en)

                # 感情ごとの処理を行う
                # 感情ごとの処理はブロッキングな処理である (各5秒)
                if emotion == "positive":
                    print u"判定結果: ポジティブ！"
                    positive_move()
                if emotion == "super_positive":
                    print u"判定結果: 超めっちゃポジティブ！！！"
                    super_positive_move()
                elif emotion == "negative":
                    print u"判定結果: ネガティブ……"
                    negative_move()

            else:
                # 認識に失敗した場合
                print(u"何も見えない")

    finally:
        # KeyboardInterrupt などで終了するときはモーターを全部リセット
        reset_all_motors()
