import cv2
import numpy as np

# image path
path = r'C:\Users\INFOKOM\Desktop\studyy\IIA4\traitementImage\shape2R.jpg'
# using imread()
imgI = cv2.imread(path)
dim=(640,360)
img=cv2.resize(imgI,dim)
#changing colormap for idexed color image
im1 = cv2.applyColorMap(img, cv2.COLORMAP_AUTUMN)
im2 = cv2.applyColorMap(img, cv2.COLORMAP_BONE)
# Display
cv2.imshow('image', np.hstack((im1, im2)))
#Converting color space
imagegray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imagehsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
imageyuv = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
imagecmyk = cv2.cvtColor(img,cv2.COLOR_BGR2YCR_CB)
# Displaying
cv2.imshow('gray', imagegray)
cv2.imshow('hsv', imagehsv)
cv2.imshow('YUV', imageyuv)
cv2.imshow('CMYK', imagecmyk)
cv2.waitKey(0);
cv2.destroyAllWindows();
cv2.waitKey(1)