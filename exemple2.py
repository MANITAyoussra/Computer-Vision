import cv2
# image path
path = r'C:\Users\INFOKOM\Desktop\studyy\IIA4\traitementImage\shape1.png'
# using imread()
img = cv2.imread(path)
# get dimensions of image
dimensions = img.shape
# height, width, number of channels in image
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
print('Image Dimension : ', dimensions)
print('Image Height : ', height)
print('Image Width : ', width)
print('Number of Channels : ', channels)
# Total number of pixels on the image
sizeImage=img.size
print('number of pixels : ', sizeImage)
# reading image to be resized
path2 = r'C:\Users\INFOKOM\Desktop\studyy\IIA4\traitementImage\natureResult.png'
# using imread()
img2 = cv2.imread(path2)
# resize image then display
img2Res=cv2.resize(img2,(width,height))
cv2.imshow('img2Res', img2Res)
cv2.waitKey(0);
cv2.destroyAllWindows();
cv2.waitKey(1)