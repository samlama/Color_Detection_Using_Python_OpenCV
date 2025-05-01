#Basic Image Manipulation
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
image=cv.imread("image.jpg")
assert image is not None, "file could not be read, check with os.path.exists()"

#Convert to grayscale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)


# Apply Gaussian Blur
blur = cv.GaussianBlur(gray, (7, 7), 0)

# 3. Canny Edge Detection
edges = cv.Canny(blur, 50, 150)
#final output
cv.imwrite('image.jpg', edges)


#code for the demonstrating all code at once to show the pictures is
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('cat.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"
 
RED = [255,255,0]

reflect = cv.copyMakeBorder(img,10,100,10,10,cv.BORDER_REFLECT)

constant= cv.copyMakeBorder(img,100,10,100,10,cv.BORDER_CONSTANT,value=RED)

plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORIGINAL')

plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')

plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()
#Note: for the last code, reference was taken from the google.