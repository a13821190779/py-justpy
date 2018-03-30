#!/usr/bin/env python
#coding=utf-8

import cv2
import numpy as np
import os
from urllib.parse import urljoin

print()


imgUrl = urljoin(os.path.abspath('./1'), './imgs/1522379284.345199.jpg')
img = cv2.imread(imgUrl, 1)
cv2.namedWindow("Image")
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
