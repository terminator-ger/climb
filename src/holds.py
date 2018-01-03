import numpy as np
import cv2 
from matplotlib import pyplot as plt


# this function is needed for the createTrackbar step downstream
def nothing(x):
    pass
    
def update(x):
### Infinite loop until we hit the escape key on keyboard
    s = cv2.getTrackbarPos(switch,'image')
    
    if s == 1:
        # get current positions of four trackbars
        l = cv2.getTrackbarPos('lower', 'image')
        u = cv2.getTrackbarPos('upper', 'image')
        ####################
        # EDGE
        edges_r = cv2.Canny(r, l,u)
        edges_g = cv2.Canny(g, l,u)
        edges_b = cv2.Canny(b, l,u)
        
        all_edges = cv2.merge((edges_r, edges_g, edges_b))
        ####################
        # CONTOUR
        ret,thresh_r = cv2.threshold(all_edges,127,255,0)
        t = cv2.cvtColor(thresh_r, cv2.COLOR_BGR2GRAY);
        
        image, contours_r, hierarchy = cv2.findContours(t, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
        
        mod_img = cv2.drawContours(img, contours_r, -1, (0,255,0), 3)
        
        cv2.imshow('image', mod_img)
        cv2.waitKey() & 0xFF


    #for i in range(1,len(contours_r)) :
#    for i in range(1,1) :
#        (x,y),radius = cv2.minEnclosingCircle(contours_r[i])
#        center = (int(x),int(y))
#        radius = int(radius)
#        img = cv2.circle(img,center,radius,(255,0,0),2)
#        cv2.imshow('canny', img)
#        k = cv2.waitKey() & 0xFF
        


#wall flat
#img = cv2.imread('D:\dev\Holds\IMG_20171119_190948.jpg')


img = cv2.imread('D:\dev\holds\IMG_20171119_191000.jpg')

#moonboard
#img = cv2.imread('D:\dev\holds\IMG_20171119_191819.jpg')

#steep flat
#img = cv2.imread('E:\dev\Holds\pano.jpg' )

#img = cv2.imread('E:\dev\Holds\pano1.jpg')



b,g,r = cv2.split(img)


# add additional blur -> smoothen crappy lenovo cam
#img = cv2.GaussianBlur(img,(5,5),0)

r = cv2.GaussianBlur(r,(5,5),0)
g = cv2.GaussianBlur(g,(5,5),0)
b = cv2.GaussianBlur(b,(5,5),0)
  
# create trackbar for canny edge detection threshold changes
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
### add lower and upper threshold slidebars to "canny"
cv2.createTrackbar('lower', 'image', 0, 255, update)
cv2.createTrackbar('upper', 'image', 0, 255, update)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1, update)

mod_img = img



gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
minLineLength = 1
maxLineGap = 1
lines = cv2.HoughLinesP(edges,1,np.pi/180,20,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
cv2.imshow('image', img)
cv2.waitKey() & 0xFF
cv2.destroyAllWindows()



        
