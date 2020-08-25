import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt

## (1) read

# Read the image. The first command line argument is the image
# image = cv2.imread(sys.argv[1])
image = cv2.imread("little_mix.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cascPath = "/Library/Python/2.7/site-packages/cv2/data/haarcascade_frontalface_default.xml"


# Create the haar cascade
face_cascade = cv2.CascadeClassifier(cascPath)
# Detect faces in the image
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor = 1.2,
    minNeighbors = 5,
    minSize = (30,30)

)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found" ,image)
cv2.waitKey(0)