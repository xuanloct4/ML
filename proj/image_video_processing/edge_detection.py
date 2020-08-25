import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt

## (1) read

# Read the image. The first command line argument is the image
# image = cv2.imread(sys.argv[1])
image = cv2.imread("bill1.png")

#convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#blur it
blurred_image = cv2.GaussianBlur(gray_image, (7,7), 0)

cv2.imshow("Orignal Image", image)


canny = cv2.Canny(blurred_image, 10, 30)
cv2.imshow("Canny with low thresholds", canny)

canny2 = cv2.Canny(blurred_image, 50, 150)
cv2.imshow("Canny with high thresholds", canny2)

cv2.waitKey(0)