import numpy as np
import cv2
from matplotlib import pyplot as plt

image= cv2.imread(r'C:\Users\INFOKOM\Desktop\studyy\IIA4\traitementImage\MiniProjet\medianBlur.jpg')
kernel = cv2.getStructuringElement(cv2.MORPH_OPEN,(3,3))
# convert image to gray
imagegray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


#seillage
(retVal, I2) = cv2.threshold(imagegray, 100, 255, cv2.THRESH_BINARY)
cv2.imshow('image',I2)
#Save image
imwrt = cv2.imwrite(r'C:\Users\INFOKOM\Desktop\studyy\IIA4\traitementImage\MiniProjet\seuillage.jpg',I2)
#ouverture
ouverture = cv2.morphologyEx(I2,cv2.MORPH_OPEN, kernel)
cv2.imshow('ouverture',ouverture)
#Save image
imwrt = cv2.imwrite(r'C:\Users\INFOKOM\Desktop\studyy\IIA4\traitementImage\MiniProjet\OUVERTURE.jpg',ouverture )
#rogner l'image filtrée
croped=ouverture[200:400,120:999]
cv2.imshow('carte_rognee',croped)
#Save image
imwrt = cv2.imwrite(r'C:\Users\INFOKOM\Desktop\studyy\IIA4\traitementImage\MiniProjet\croped.jpg',croped )
#detect contours
SobelC=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
SobelL=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
W1=abs(cv2.filter2D(croped,cv2.CV_64F,SobelC))
W2=abs(cv2.filter2D(croped,cv2.CV_64F,SobelL))
contours=W1+W2
cv2.imshow('Contours ',contours )
#Save image
imwrt =cv2.imwrite(r'C:\Users\INFOKOM\Desktop\studyy\IIA4\traitementImage\Mini
Projet\contours.jpg',contours)
cv2.waitKey(0)
# closing all open windows
cv2.destroyAllWindows() 