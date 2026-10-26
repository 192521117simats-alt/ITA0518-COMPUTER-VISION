import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("image.jpg")

# Check whether the image is loaded
if image is None:
    print("Error: Could not load image")
    exit()

# Get original image size
height, width = image.shape[:2]

# Resize to bigger size
bigger_image = cv2.resize(
    image,
    (width * 2, height * 2),
    interpolation=cv2.INTER_LINEAR
)

# Resize to smaller size
smaller_image = cv2.resize(
    image,
    (width // 2, height // 2),
    interpolation=cv2.INTER_AREA
)

# Display the images
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(bigger_image, cv2.COLOR_BGR2RGB))
plt.title("Bigger Image")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(smaller_image, cv2.COLOR_BGR2RGB))
plt.title("Smaller Image")
plt.axis("off")

plt.tight_layout()
plt.show()