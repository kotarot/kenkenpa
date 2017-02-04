#!/usr/bin/python
# -*- coding: utf-8 -*-
from recognition import *

if __name__ == '__main__':
    # 物体認識モジュールのサンプル
    while True:
        (label_en, label_ja, prob) = recognize()

        if prob > 0.2:
            print(u"{} ({})が見える (prob:{})".format(label_ja, label_en, prob))
        else:
            print(u"何も見えない")
