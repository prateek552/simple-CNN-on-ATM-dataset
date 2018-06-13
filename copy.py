# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 18:51:52 2018

@author: Heller
"""

import os
import cv2
count=0
dir=os.listdir('multiple ab/')
for fol in dir:
    dir2='multiple ab/'+fol
    print (dir2)
    dir3=os.listdir(dir2)
    for file in dir3:
        count=count+1
        print (count)
        print (file)
        f=cv2.imread(dir2+'/'+file)
        cv2.imwrite('multiple ab/mutiple ab%d.jpg' %count,f)
        