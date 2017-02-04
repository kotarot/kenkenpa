#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2

CASCADE_PATH = "/usr/local/Cellar/opencv3/3.2.0/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(CASCADE_PATH)

def detectFace(image):
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.07, minNeighbors=9, minSize=(10, 10))
    return facerect

if __name__ == "__main__":
    file_name = "face.jpg"
    print("detect face on file:"+file_name)

    # 画像のロード
    image = cv2.imread(file_name)
    if image is None:
        # 読み込み失敗
        print("image is None")
        exit(1)

    # 顔画像抽出
    facerect_list = detectFace(image)
    if len(facerect_list) > 0:
        print u"There is a Face!!!"
    else:
        print u"No Face!!!"
