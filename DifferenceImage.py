import cv2

# Load the images
img1 = cv2.imread('comel.jpg')
img2 = cv2.imread('comel4.jpg')

# Convert the images to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Compute the absolute difference between the two images
diff = cv2.absdiff(gray1, gray2)

# Show the Difference Image
cv2.imshow('Difference Image', diff)
cv2.waitKey(0)
cv2.destroyAllWindows()





