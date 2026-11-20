import cv2

# Read the input image
image = cv2.imread("image.jpg")

if image is None:
    print("Error: Cannot load image.jpg")
    exit()

# Get text from the user
text = input("Enter the text to display on the image: ")

# Set text properties
position = (50, 100)
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
color = (0, 0, 255)  # Red color
thickness = 2

# Add text to the image
cv2.putText(
    image,
    text,
    position,
    font,
    font_scale,
    color,
    thickness
)

# Display the output image
cv2.imshow("Image with Text", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the output image
cv2.imwrite("experiment35_output.jpg", image)

print("Output saved as experiment35_output.jpg")
