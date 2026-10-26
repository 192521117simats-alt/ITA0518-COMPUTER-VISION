import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("image.jpg")

# Check whether the image is loaded
if image is None:
    print("Error: Could not load image")
    exit()

# Copy the original image
watermarked_image = image.copy()

# Add watermark text
cv2.putText(
    watermarked_image,
    "WATERMARK",
    (50, image.shape[0] - 30),
    cv2.FONT_HERSHEY_SIMPLEX,
    1.5,
    (255, 255, 255),
    3,
    cv2.LINE_AA
)

# Display original and watermarked images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(watermarked_image, cv2.COLOR_BGR2RGB))
plt.title("Watermarked Image")
plt.axis("off")

plt.tight_layout()
plt.show()