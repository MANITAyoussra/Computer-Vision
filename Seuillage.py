import cv2
import numpy as np
import matplotlib.pyplot as plt

path = r'C:\Users\INFOKOM\Desktop\studyy\IIA4\traitementImage\TP2\ coinsSP.png'
I= cv2.imread(path,0)
#cv2.imshow('image1',I)
f1=plt.figure(1)
f1=plt.hist(I.ravel(),256,[0,256])

I2=cv2.threshold(I, 50, 256,cv2.THRESH_BINARY)
#cv2.imshow('image',I2)
plt.show()