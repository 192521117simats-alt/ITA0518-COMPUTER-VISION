import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("image.jpg")

# Check whether the image is loaded
if image is None:
    print("Error: Could not load image")
    exit()

# Get image dimensions
height, width = image.shape[:2]

# Define four points from the original image
src_points = np.float32([
    [0, 0],
    [width - 1, 0],
    [width - 1, height - 1],
    [0, height - 1]
])

# Define four destination points
dst_points = np.float32([
    [50, 50],
    [width - 50, 0],
    [width - 1, height - 1],
    [0, height - 50]
])

# Create perspective transformation matrix
matrix = cv2.getPerspectiveTransform(src_points, dst_points)

# Apply perspective transformation
perspective_image = cv2.warpPerspective(
    image,
    matrix,
    (width, height)
)

# Display original and transformed images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(perspective_image, cv2.COLOR_BGR2RGB))
plt.title("Perspective Transformed Image")
plt.axis("off")

plt.tight_layout()
plt.show()