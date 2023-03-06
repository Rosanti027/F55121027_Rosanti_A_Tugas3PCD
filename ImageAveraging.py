import cv2
import numpy as np

# Load the images
img1 = cv2.imread('comel4.jpg')
img2 = cv2.imread('comel.jpg')

# Average the images
average = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

# Show the Average Image
cv2.imshow('Average Image', average)
cv2.waitKey(0)
cv2.destroyAllWindows()