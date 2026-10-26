import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("image.jpg")

# Check whether the image is loaded
if image is None:
    print("Error: Could not load image")
    exit()

# Create a copy of the image
result_image = image.copy()

# Convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load the pre-trained Haar cascade classifier
watch_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Detect objects using the loaded classifier
objects = watch_cascade.detectMultiScale(
    gray_image, scaleFactor=1.1, minNeighbors=5
)

# Draw rectangles around detected objects
for (x, y, w, h) in objects:
    cv2.rectangle(
        result_image, (x, y), (x + w, y + h), (0, 255, 0), 2
    )

# Display the images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB))
plt.title("Detection Result")
plt.axis("off")

plt.tight_layout()
plt.show()