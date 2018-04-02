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

# # print(getPathOfPattern(patternName))

imgUrl = urljoin(os.path.abspath('./1'), './imgs/1522669385.6072042.jpg')

img = cv2.imread(imgUrl)

# cv2.namedWindow(myimg, cv2.WINDOW_NORMAL)
# cv2.imshow(myimg, img)

# # 写入图片
# # cv2.imwrite('messigray.png',img)

# key = cv2.waitKey(0)

# if key == 27:
#     cv2.destroyAllWindows()
# elif key == ord('s'):
#     cv2.imwrite('save.jpg', img)
#     cv2.destroyAllWindows()

# 摄像头部分
# cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 640)
# if cap.isOpened():
#     while (True):
#         # Capture frame-by-frame
#         ret, frame = cap.read()

#         # Our operations on the frame come here
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#         # Display the resulting frame
#         cv2.imshow(myvideo, gray)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # When everything done, release the capture
#     cap.release()
#     cv2.destroyAllWindows()
# else:
#     print('not init capture, reload please')


def faceFn(frameImg):
    # 创建classifier, 有空格的路径会报错
    clf = cv2.CascadeClassifier(getPathOfPattern(patternName))
    gray = cv2.cvtColor(frameImg, cv2.COLOR_BGR2GRAY)
    # 识别面部
    faces = clf.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        cv2.rectangle(frameImg, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return frameImg


cap = cv2.VideoCapture(0)
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Be sure to use the lower case
# out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (width, height))

ret, frame = cap.read()
cv2.imshow(myvideo, frame)
while (cap.isOpened()):
    #读取帧摄像头
    ret, frame = cap.read()
    if ret == True:
        print(123)
        #输出当前帧
        # frame = faceFn(frame)
        # out.write(frame)

        # cv2.imshow('My Camera', frame)


        # Our operations on the frame come here
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow(myvideo, gray)

        #键盘按 Q 退出
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break
    else:
        break

# 释放资源
cv2.release()
cv2.destroyAllWindows()