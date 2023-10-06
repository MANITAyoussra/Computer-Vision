import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt  
import matplotlib.image as mpimg
image= cv.imread(r'C:\Users\INFOKOM\Desktop\studyy\IIA4\traitementImage\MiniProjet\cartebruitee.png')
# filtre median
img=cv.medianBlur(image, 5)
cv.imshow("img",img)
# save image
imwrt = cv.imwrite(r'C:\Users\INFOKOM\Desktop\studyy\IIA4\traitementImage\MiniProjet\medianBlur.jpg', img)  
if imwrt:
 print('Image is successfully saved.')


cv.waitKey(0)
# closing all open windows
cv.destroyAllWindows()
