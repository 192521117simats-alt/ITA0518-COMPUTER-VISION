import cv2
import matplotlib.pyplot as plt

# Function to analyze the color histogram
def analyze_histogram(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert BGR image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Calculate histograms for Red, Green and Blue channels
    red_hist = cv2.calcHist([image], [2], None, [256], [0, 256])
    green_hist = cv2.calcHist([image], [1], None, [256], [0, 256])
    blue_hist = cv2.calcHist([image], [0], None, [256], [0, 256])

    # Display the original image
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(image_rgb)
    plt.title("Original Image")
    plt.axis("off")

    # Display the color histogram
    plt.subplot(1, 2, 2)
    plt.plot(red_hist, label="Red")
    plt.plot(green_hist, label="Green")
    plt.plot(blue_hist, label="Blue")

    plt.title("Color Histogram")
    plt.xlabel("Color Level")
    plt.ylabel("Number of Pixels")
    plt.legend()

    plt.tight_layout()
    plt.show()


# Call the function
analyze_histogram("image.jpg")