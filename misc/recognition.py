#!/usr/bin/python
# -*- coding: utf-8 -*-
from inception_v3 import *
import cv2
import time
import picamera
import sys
import json

if __name__ == '__main__':
    model = InceptionV3(include_top=True, weights='imagenet')
    # cam = cv2.VideoCapture(0)
    camera = picamera.PiCamera()
    img_path = "capture.jpg"

    with open('imagenet_class_index.json', 'r') as f:
        obj = json.load(f)
        label_dict = {i['en']: i['ja'] for i in obj}

    while (True):
        # ret, frame = cam.read()
        ##cv2.imshow("Show FLAME Image", frame)
        #cv2.imwrite("temp.png", frame)
        camera.capture(img_path)
        img = image.load_img(img_path, target_size=(299, 299))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        preds = model.predict(x)
        recognize = decode_predictions(preds)
        ##print(recognize)
        label_en = recognize[0][0][1]
        label_ja = label_dict[label_en]
        prob = recognize[0][0][2]
        if (prob > 0):
            print(u"{} ({})が見える (prob:{})".format(label_ja, label_en, prob))
        else:
            print(u"何も見えない")
        time.sleep(0.5)

    #cam.release()
    #cv2.destroyAllWindows()
