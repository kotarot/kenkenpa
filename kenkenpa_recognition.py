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

if __name__ == '__main__':
    # 物体認識モデルのロード
    model = InceptionV3(include_top=True, weights='imagenet')
    # cam = cv2.VideoCapture(0)
    # PiCamera初期化
    camera = picamera.PiCamera()    

    # 物体labelをenからjaに変換する辞書のロード
    with open('imagenet_class_index.json', 'r') as f:
        obj = json.load(f)
        label_dict = {i['en']: i['ja'] for i in obj}

    while (True):
        # ret, frame = cam.read()
        ##cv2.imshow("Show FLAME Image", frame)
        #cv2.imwrite("temp.png", frame)

        start = time.time()
        
        # カメラ画像を一時ファイルに出力
        camera.capture(TMP_IMG_PATH)
        
        #elapsed_time = time.time() - start
        #print (u"captureにかかる時間:{0}".format(elapsed_time)) + "[sec]"
        #start = time.time()
        
        # 画像のロード
        img = image.load_img(TMP_IMG_PATH, target_size=(299, 299))
        
        #elapsed_time = time.time() - start
        #print (u"imgのロードにかかる時間:{0}".format(elapsed_time)) + "[sec]"
        #start = time.time()
        
        cv2image = cv2.imread(TMP_IMG_PATH)
        
        #elapsed_time = time.time() - start
        #print (u"cv2imgのロードにかかる時間:{0}".format(elapsed_time)) + "[sec]"
        #start = time.time()

        # 物体認識
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
            
        #elapsed_time = time.time() - start
        #print (u"物体認識にかかる時間:{0}".format(elapsed_time)) + "[sec]"
        #start = time.time()
            
        # facerect_list = detectFace(cv2image)
        # if len(facerect_list) > 0:
        #     print u"顔が見える"
        # else:
        #     print u"顔は見えない"
            
        # elapsed_time = time.time() - start
        # print (u"顔認識にかかる時間:{0}".format(elapsed_time)) + "[sec]"
        # start = time.time()

    #cam.release()
    #cv2.destroyAllWindows()