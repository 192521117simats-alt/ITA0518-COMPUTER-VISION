import cv2
import matplotlib.pyplot as plt
# Read the input image
image = cv2.imread("image.jpg")
if image is None:
    print("Error: Cannot load image.jpg")
    exit()
# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Apply binary thresholding
threshold_value = 127
max_value = 255
ret, segmented = cv2.threshold(
    gray, threshold_value, max_value, cv2.THRESH_BINARY
)
# Display original and segmented images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(segmented, cmap="gray")
plt.title("Segmented Image")
plt.axis("off")
plt.tight_layout()
plt.show()
