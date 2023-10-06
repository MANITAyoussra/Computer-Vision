import cv2
# image path
path = r'C:\Users\INFOKOM\Desktop\studyy\IIA4\traitementImage\nature.png'
# using imread()
img = cv2.imread(path)
# displaying the image
cv2.imshow('image', img)
# save image
imwrt = cv2.imwrite(r'C:\Users\INFOKOM\Desktop\studyy\IIA4\traitementImage\natureResult.png', img)
cv2.imshow('imageSaved', img)
if imwrt:
 print('Image is successfully saved.')
cv2.waitKey(0);
cv2.destroyAllWindows();
cv2.waitKey(1)