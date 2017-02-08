# -*- coding: utf-8 -*-
from inception_v3 import *
import cv2
import time

if __name__ == '__main__':
    model = InceptionV3(include_top=True, weights='imagenet')
    cam = cv2.VideoCapture(0)
    import sys
    import json

    with open('imagenet_class_index.json', 'r') as f:
        obj = json.load(f)
        label_dict = {i['en']: i['ja'] for i in obj}

    while (True):
        ret, frame = cam.read()
        ##cv2.imshow("Show FLAME Image", frame)
        cv2.imwrite("temp.png", frame)
        img_path = "temp.png"
        img = image.load_img(img_path, target_size=(299, 299))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        preds = model.predict(x)
        recognize = decode_predictions(preds)
        ##print(recognize)
        label = label_dict[recognize[0][0][1]]
        prob = recognize[0][0][2]
        if (prob > 0.2):
            print("{}が見える (prob:{})".format(label, prob))
        else:
            print("何も見えない")
        time.sleep(1)

    cam.release()
    cv2.destroyAllWindows()
