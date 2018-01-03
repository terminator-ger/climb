# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 13:10:59 2017

@author: Michael
"""
import cv2

def load(select):
    
    switch = {
            #wall flat
            0: 'D:\dev\Holds\IMG_20171119_190948.jpg',
            #moonboard
            1: 'D:\dev\Holds\IMG_20171119_191819.jpg',
            #steep wall
            2: 'D:\dev\Holds\IMG_20171119_190941.jpg',
    }
    return cv2.imread(switch.get(select,"otherwise"))
