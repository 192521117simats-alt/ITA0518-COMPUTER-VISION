import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("image.jpg")

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply histogram equalization
equalized_image = cv2.equalizeHist(gray_image)

# Display original grayscale image
plt.subplot(2, 2, 1)
plt.imshow(gray_image, cmap="gray")
plt.title("Original Grayscale Image")
plt.axis("off")

# Display histogram equalized image
plt.subplot(2, 2, 2)
plt.imshow(equalized_image, cmap="gray")
plt.title("Histogram Equalized Image")
plt.axis("off")

# Display original histogram
plt.subplot(2, 2, 3)
plt.hist(gray_image.ravel(), 256, [0, 256])
plt.title("Original Histogram")
plt.xlabel("Intensity")
plt.ylabel("Frequency")

# Display equalized histogram
plt.subplot(2, 2, 4)
plt.hist(equalized_image.ravel(), 256, [0, 256])
plt.title("Equalized Histogram")
plt.xlabel("Intensity")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()