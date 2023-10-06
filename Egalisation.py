import cv2
import numpy as np
import matplotlib.pyplot as plt

path = r'C:\Users\INFOKOM\Desktop\studyy\IIA4\traitementImage\TP2\pout.tif '
I= cv2.imread(path,0)
f1=plt.figure(1)
f1=plt.hist(I.ravel(),256,[0,256])
I2=cv2.equalizeHist(I)
f2=plt.figure(2)
f2=plt.hist(I2.ravel(),256,[0,256])

I3=cv2.add(I,-13)
cv2.imshow('image',I3)
plt.show()