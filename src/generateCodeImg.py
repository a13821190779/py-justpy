import string
import random
import cv2
import numpy as np
import os

randomLetter = ' '.join(random.sample(string.ascii_letters, 4))

img = np.zeros((50, 140, 3))

font = cv2.FONT_HERSHEY_SIMPLEX
h = img.shape[0]
w = img.shape[1]
print(h)
print(w)
print(font)


cv2.putText(img, randomLetter, (5, 30), font, 1, (0, 100, 0), 2, cv2.LINE_AA)

cv2.imwrite(os.path.join(os.path.abspath('.'), 'code.jpg'), img)