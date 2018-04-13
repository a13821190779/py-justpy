import cv2
import numpy as np
import os

imageName = 'IMAGE'
curRootPath = os.path.abspath('./')
imgUrl = os.path.join(curRootPath, 'imgs/index.jpg')
# cv2.imread need abslute path!!
img = cv2.imread(imgUrl, 1)
h = img.shape[0]
w = img.shape[1]

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (w - 130, 30), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

cv2.imshow(imageName, img)
cv2.waitKey(0)
cv2.destroyAllWindows()

