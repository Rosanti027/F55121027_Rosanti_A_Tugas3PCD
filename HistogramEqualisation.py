import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load grayscale image
img = cv2.imread('comel.jpg', cv2.IMREAD_GRAYSCALE)

# Calculate histogram
hist, bins = np.histogram(img.flatten(), 256, [0, 256])

# Calculate cumulative distribution function (CDF)
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max() / cdf.max()

# Perform histogram equalization
equ = cv2.equalizeHist(img)

# Calculate new histogram
hist_equ, bins_equ = np.histogram(equ.flatten(), 256, [0, 256])

# Plot original and equalized images and their histograms
fig, axs = plt.subplots(2, 2, figsize=(8, 8))
axs[0, 0].imshow(img, cmap='gray')
axs[0, 0].set_title('Original Image')
axs[0, 1].hist(img.flatten(), 256, [0, 256], color='r')
axs[0, 1].set_title('Original Histogram')
axs[1, 0].imshow(equ, cmap='gray')
axs[1, 0].set_title('Equalized Image')
axs[1, 1].hist(equ.flatten(), 256, [0, 256], color='r')
axs[1, 1].set_title('Equalized Histogram')
plt.show()