import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("image.jpg")

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect edges using Canny function
canny_image = cv2.Canny(gray_image, 100, 200)

# Display original image
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

# Display Canny edge image
plt.subplot(1, 2, 2)
plt.imshow(canny_image, cmap="gray")
plt.title("Canny Edge Image")
plt.axis("off")

plt.show()