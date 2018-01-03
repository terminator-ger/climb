# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 01:29:23 2017

@author: Michael
"""
import numpy as np
import cv2 

#wall flat
#img = cv2.imread('D:\dev\Holds\IMG_20171119_190948.jpg')

img = cv2.imread('D:\dev\holds\IMG_20171119_191000.jpg',0)

#moonboard
#img = cv2.imread('D:\dev\holds\IMG_20171119_191819.jpg')

#steep flat
#img = cv2.imread('E:\dev\Holds\pano.jpg' )

#img = cv2.imread('E:\dev\Holds\pano1.jpg')



#img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20, param1=50,param2=30,minRadius=7,maxRadius=30)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',cimg)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()