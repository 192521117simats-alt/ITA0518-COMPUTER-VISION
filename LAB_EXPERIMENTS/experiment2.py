import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("image.jpg")

# Apply Gaussian Blur
blur_image = cv2.GaussianBlur(image, (15, 15), 0)

# Display original image
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

# Display blurred image
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(blur_image, cv2.COLOR_BGR2RGB))
plt.title("Gaussian Blurred Image")
plt.axis("off")

plt.show()