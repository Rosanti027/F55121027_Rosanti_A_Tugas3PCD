import cv2
import numpy as np

#masukkan gambar
img1 = cv2.imread('kiyowo.jpg')
img1 = cv2.resize(img1, (595, 489))
img2 = cv2.imread('comel.jpg')
img2 = cv2.resize(img2,(595, 489))

#ubah gambar ke grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#Subtract gambar grayscale
diff = cv2.subtract(gray1, gray2)

cv2.imshow('img1', img1)
cv2.imshow('img2',img2)
cv2.imshow('Difference', diff)
cv2.waitKey(0)
cv2.destroyAllWindows()
