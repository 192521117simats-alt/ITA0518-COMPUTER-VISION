import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("image.jpg")

# Check whether the image is loaded
if image is None:
    print("Error: Could not load image")
    exit()

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create a kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# Apply dilation
dilated_image = cv2.dilate(gray_image, kernel, iterations=1)

# Display original and dilated images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(gray_image, cmap="gray")
plt.title("Original Grayscale Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(dilated_image, cmap="gray")
plt.title("Dilated Image")
plt.axis("off")

plt.tight_layout()
plt.show()