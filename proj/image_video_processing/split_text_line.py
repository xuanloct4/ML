import cv2
import numpy as np
from matplotlib import pyplot as plt

minH = 10

## (1) read
img = cv2.imread("bill.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow('Origin image', img)
# cv2.imshow('Gray image', gray)
# cv2.waitKey(0)

## (2) threshold
th, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
# th, threshed = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)

## (3) minAreaRect on the nozeros
pts = cv2.findNonZero(threshed)
ret = cv2.minAreaRect(pts)

(cx,cy), (w,h), ang = ret
if w>h:
    w,h = h,w
    ang += 90

## (4) Find rotated matrix, do rotation
M = cv2.getRotationMatrix2D((cx,cy), ang, 1.0)
rotated = cv2.warpAffine(threshed, M, (img.shape[1], img.shape[0]))


# crop_img = img[0:60, 0:150]
# cv2.imshow('Gray image', gray)
# cv2.waitKey(0)

## (5) find and draw the upper and lower boundary of each lines
hist = cv2.reduce(rotated,1, cv2.REDUCE_AVG).reshape(-1)
# hist = cv2.reduce(gray,1, cv2.REDUCE_AVG).reshape(-1)

# th = 2
th = 0
H,W = img.shape[:2]
uppers = [y for y in range(H-1) if hist[y]<=th and hist[y+1]>th]
lowers = [y for y in range(H-1) if hist[y]>th and hist[y+1]<=th]

rotated = cv2.cvtColor(rotated, cv2.COLOR_GRAY2BGR)
#
for y in uppers:
    cv2.line(rotated, (0,y), (W, y), (255,0,0), 1)
    # cv2.line(img, (0,y), (W, y), (255,0,0), 1)

for y in lowers:
    cv2.line(rotated, (0,y), (W, y), (0,255,0), 1)
    # cv2.line(img, (0,y), (W, y), (0,255,0), 1)

# Normalize
normalizedUppers = []
normalizedLowers = []
lower = upper = 0
j = -1
for i in range(0,len(uppers), 1):
    if j < i:
        j = i
        upper = uppers[i]
        lower = lowers[i]
        if lowers[j] - uppers[j] >= minH:
            normalizedUppers.append(upper)
            normalizedLowers.append(lower)
        while j <= len(uppers)-1:
            if lowers[j] - uppers[j] < minH:
                if j == 0:
                    normalizedUppers.append(uppers[j])
                    normalizedLowers.append(lowers[j])
                    j = j+1
                elif j == len(uppers)-1:
                    if len(normalizedUppers) == 0:
                        normalizedUppers.append(uppers[j])
                    if len(normalizedLowers) == 0:
                        normalizedLowers.append(lowers[j])
                    else:
                        normalizedLowers[len(normalizedLowers)-1] = lowers[j]
                    break

                elif uppers[j]-lowers[j-1] < uppers[j+1]-lowers[j]:
                    if len(normalizedUppers) == 0:
                        normalizedUppers.append(uppers[j])
                    if len(normalizedLowers) == 0:
                        normalizedLowers.append(lowers[j])
                    else:
                        normalizedLowers[len(normalizedLowers)-1] = lowers[j]
                    j = j+1
                elif uppers[j]-lowers[j-1] >= uppers[j+1]-lowers[j]:
                    normalizedUppers.append(uppers[j])
                    normalizedLowers.append(lowers[j])
                    j = j+1
                # else:
                #     if len(normalizedUppers) == 0:
                #         normalizedUppers.append(uppers[j])
                #     if len(normalizedLowers) == 0:
                #         normalizedLowers.append(lowers[j])
                #     else:
                #         normalizedLowers[len(normalizedLowers)-1] = lowers[j]
                #     j = j+1
            else:
                j = j-1
                break

for i in range(0,len(normalizedUppers), 1):
    crop_img = img[normalizedUppers[i]-1:normalizedLowers[i]+1, 0:W]
    img_piece = "result//result" + str(i) +".png"
    cv2.imwrite(img_piece, crop_img)


# cv2.imwrite("result_.png", img)
cv2.imwrite("result.png", rotated)
