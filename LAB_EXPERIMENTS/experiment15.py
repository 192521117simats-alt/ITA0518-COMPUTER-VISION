import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("image.jpg")

# Check whether the image is loaded
if image is None:
    print("Error: Could not load image")
    exit()

# Convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Harris Corner Detection
gray_image = cv2.GaussianBlur(gray_image, (3, 3), 0)

corners = cv2.cornerHarris(
    gray_image,
    blockSize=2,
    ksize=3,
    k=0.04
)

# Dilate corner points for better visibility
corners = cv2.dilate(corners, None)

# Mark detected corners in red
result = image.copy()
result[corners > 0.01 * corners.max()] = [0, 0, 255]

# Display original and corner-detected images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.title("Harris Corner Detection")
plt.axis("off")

plt.tight_layout()
plt.show()