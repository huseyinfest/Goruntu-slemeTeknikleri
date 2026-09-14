import cv2 as cv
import numpy as np

img = cv.imread('sabriabi.jpg')
cv.imshow('Sabri Abi', img)
cv.waitKey(0)
cv.destroyAllWindows()