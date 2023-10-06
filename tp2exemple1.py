import cv2
import numpy as np
import matplotlib.pyplot as plt

path = r'C:\Users\INFOKOM\Desktop\studyy\IIA4\traitementImage\TP2\pout.tif'
I= cv2.imread(path)
#cv2.calcHist([I],[0], None, [256], [0,256])
f1=plt.figure(1)



plt.title('histogramme')
h=plt.hist(I.ravel(),256,[0,256])
#moy :print(np.max(h[0])/I.size)
print(np.max(h[0]))
f2=plt.figure(2)
f2=plt.hist(I.ravel(),64,[0,256])
f3=plt.figure(3)
f3=plt.hist(I.ravel(),32,[0,256])
f4=plt.figure(4)
f4=plt.hist(I.ravel(),128,[0,256])
plt.show()
