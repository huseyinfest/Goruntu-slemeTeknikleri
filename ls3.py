import cv2

img_gray = cv2.imread('sabriabi.jpg', cv2.IMREAD_GRAYSCALE)

colormap_viridis = cv2.applyColorMap(img_gray, cv2.COLORMAP_VIRIDIS)

cv2.imshow('VIRIDIS Haritasi', colormap_viridis)

cv2.waitKey(0)
cv2.destroyAllWindows()