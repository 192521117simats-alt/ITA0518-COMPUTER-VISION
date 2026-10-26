import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("image.jpg")

# Check whether the image is loaded
if image is None:
    print("Error: Could not load image")
    exit()

# Get image dimensions
height, width = image.shape[:2]

# Define Region of Interest (ROI)
x1, y1 = width // 4, height // 4
x2, y2 = width // 2, height // 2

# Crop the ROI
roi = image[y1:y2, x1:x2]

# Copy the ROI
copied_roi = roi.copy()

# Paste the ROI onto another location in the image
result_image = image.copy()
result_image[0:copied_roi.shape[0],
             0:copied_roi.shape[1]] = copied_roi

# Display images
plt.figure(figsize=(12, 5))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))
plt.title("Cropped ROI")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB))
plt.title("Image After Copy and Paste")
plt.axis("off")

plt.tight_layout()
plt.show()