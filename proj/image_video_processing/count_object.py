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

# Show both our images
cv2.imshow("Original image", image)
cv2.imshow("Blurred image", blurred_image)

# Run the Canny edge detector
canny = cv2.Canny(blurred_image, 30, 100)
cv2.imshow("Canny", canny)

im, contours, hierarchy= cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Number of objects found = ", len(contours))

cv2.drawContours(image, contours, -1, (0,255,0), 2)
cv2.imshow("objects Found", image)
cv2.waitKey(0)