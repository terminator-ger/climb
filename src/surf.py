# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 14:32:06 2017

@author: Michael
"""



import cv2
import numpy as np
import tsvimage
from matplotlib import pyplot as plt


img = tsvimage.load(1);
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


# Initiate STAR detector
orb = cv2.ORB_create()

# find the keypoints with ORB
kp = orb.detect(img,None)

# compute the descriptors with ORB
kp, des = orb.compute(img, kp)

# draw only keypoints location,not size and orientation
img2 = cv2.drawKeypoints(img,kp,color=(0,255,0), flags=0)
plt.imshow(img2),plt.show()
