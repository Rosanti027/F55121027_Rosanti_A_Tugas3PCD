import cv2
import numpy as np

# membaca citra
img = cv2.imread('comel2.jpg')

# ukuran kernel
ksize = 5

# kernel filter rata-rata
kernel = np.ones((ksize,ksize), np.float32)/(ksize*ksize)

# menerapkan filter rata-rata
dst = cv2.filter2D(img, -1, kernel)

# menampilkan citra asli dan hasil filter rata-rata
cv2.imshow('Citra Asli', img)
cv2.imshow('Hasil Filter Rata-rata', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()