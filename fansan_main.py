#!/usr/bin/python
# -*- coding: utf-8 -*-
from recognition import *
from motorutil import *
from collections import defaultdict


def default_emotion(key):
    if len(key) % 2 == 0:
        return "positive"
    else:
        return "negative"


emotion_map = defaultdict(str, {"banana": "positive", "orange": "negative"})

if __name__ == '__main__':
    # ファンさんのデモを実行
    while True:
        (label_en, label_ja, prob) = recognize()
        if prob > 0.15:
            print(u"{} ({}) が見える (prob:{})".format(label_ja, label_en, prob))
        else:
            print(u"何も見えない")

        emotion = emotion_map[label_en]
        if emotion == "":
            emotion = default_emotion(label_en)

        if emotion == "positive":
            pass
        elif emotion == "negative":
            pass
