#!/usr/bin/python
# -*- coding: utf-8 -*-
from inception_v3 import *
import cv2
import time
import picamera
import sys
import json

# from gensim.models.word2vec import Word2Vec, Text8Corpus

# opencv face recognition model
CASCADE_PATH = "/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(CASCADE_PATH)


def detectFace(image):
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.07, minNeighbors=9, minSize=(10, 10))
    return facerect


# カメラの画像の一時ファイルの名称
TMP_IMG_PATH = "capture.jpg"

# 物体認識モデルのロード
model = InceptionV3(include_top=True, weights='imagenet')
# PiCamera初期化
camera = picamera.PiCamera()
# 物体labelをenからjaに変換する辞書のロード
with open('imagenet_class_index.json', 'r') as f:
    obj = json.load(f)
    label_dict = {i['en']: i['ja'] for i in obj}


def recognize():
    u"""カメラの映像から一般物体認識を実行し、(英語ラベル、日本語ラベル、確率値) を返す"""
    camera.capture(TMP_IMG_PATH)
    img = image.load_img(TMP_IMG_PATH, target_size=(299, 299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    recognize = decode_predictions(preds)
    label_en = recognize[0][0][1]
    label_ja = label_dict[label_en]
    prob = recognize[0][0][2]
    return (label_en, label_ja, prob)
