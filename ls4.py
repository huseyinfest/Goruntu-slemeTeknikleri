import cv2 as cv
import numpy as np

img = cv.imread('sabriabi.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image', gray)
cv.waitKey(0)
cv.destroyAllWindows()