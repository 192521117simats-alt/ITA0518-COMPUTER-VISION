import cv2
import numpy as np

# Read the input image
image = cv2.imread("image.jpg")

if image is None:
    print("Error: Cannot load image.jpg")
    exit()

# Convert image from BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define foreground color range (green)
lower = np.array([35, 40, 40])
upper = np.array([85, 255, 255])

# Create a mask for the selected color
mask = cv2.inRange(hsv, lower, upper)

# Extract the foreground
foreground = cv2.bitwise_and(image, image, mask=mask)

# Display results
cv2.imshow("Original Image", image)
cv2.imshow("Foreground Mask", mask)
cv2.imshow("Extracted Foreground", foreground)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the output
cv2.imwrite("experiment37_output.jpg", foreground)
