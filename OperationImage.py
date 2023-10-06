import cv2
import numpy as np
path = r'C:\Users\INFOKOM\Desktop\studyy\IIA4\traitementImage\shape1.png'
# using imread()
img = cv2.imread(path)
# get dimensions of image
dimensions = img.shape
# height, width, number of channels in image
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]

path2 = r'C:\Users\INFOKOM\Desktop\studyy\IIA4\traitementImage\nature.png'
img2 = cv2.imread(path2)
img2Res=cv2.resize(img2,(width,height))

addition=cv2.add(img, img2Res)
sub=cv2.subtract(img, img2Res)

cv2.imshow('img2Res', img2Res)
cv2.imshow('addition',addition)
cv2.imshow('sub',sub)


img1 = np.ones((300,500),dtype="uint8")
img2 = np.zeros((300,500),dtype="uint8")

img1[100:160,200:260]=255
img2[140:220,220:300]=255
#0= noir
#255=blanc
resultat_add = cv2.bitwise_and(img2, img1);
resultat_or = cv2.bitwise_or(img2, img1);
resultat_xor = cv2.bitwise_xor(img2, img1);
resultat_not = cv2.bitwise_not(img2);


cv2.imshow('resultat_add',resultat_add)
cv2.imshow('resultat_or ',resultat_or )
cv2.imshow('resultat_xor ',resultat_xor )
cv2.imshow('resultat_not  ',resultat_not  )

cv2.waitKey(0);
cv2.destroyAllWindows();
cv2.waitKey(1)