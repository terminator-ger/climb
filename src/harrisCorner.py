# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 13:10:49 2017

@author: Michael
"""

import cv2
import numpy as np
import tsvimage

img = tsvimage.load(1);

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,20,3,0.01)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()