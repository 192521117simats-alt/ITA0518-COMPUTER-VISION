import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("image.jpg")

# Check whether the image is loaded
if image is None:
    print("Error: Could not load image")
    exit()

# Rotate the image 270 degrees clockwise
rotated_image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Display original and rotated images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB))
plt.title("270 Degree Clockwise Rotated Image")
plt.axis("off")

plt.tight_layout()
plt.show()