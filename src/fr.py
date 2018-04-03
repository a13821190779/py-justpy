#!/usr/bin/env python
#coding=utf-8

import cv2
import numpy as np
import os
from urllib.parse import urljoin
from utils.getPathOfPattern import getPathOfPattern
# 绘图框架
from matplotlib import pyplot as plt

myimg = 'myimg'
myvideo = 'myvideo'
patternName = 'haarcascade_frontalface_default.xml'
xmlFile = getPathOfPattern(patternName)

# 摄像头部分
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 640)
color = (0, 255, 0)

classfier = cv2.CascadeClassifier(xmlFile)
while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        faceRects = classfier.detectMultiScale(
            frame, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))

        # if len(faceRects) > 0:
        #     print('%s张脸' % (len(faceRects)))
        #     print(faceRects)
        #     for face in faceRects:
        #         x, y, w, h = face
        #         # # 画方块 左上、右下两个定点，颜色，粗细
        #         cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10),
        #                     color, 3)
        
        if len(faceRects) > 1:
            os.system("""osascript -e 'display notification "小心背后" with title "标题"'""")

        # Display the resulting frame
        cv2.imshow(myvideo, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print('not init capture, reload please')
cap.release()
cv2.destroyAllWindows()
