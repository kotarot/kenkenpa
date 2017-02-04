#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import json

if __name__ == '__main__':
    with open('imagenet_class_index.json', 'r') as f:
        obj = json.load(f)
        label_dict = [i['ja'] + " (en: {})".format(i['en']) for i in obj]

    for line in label_dict:
        print(line)
