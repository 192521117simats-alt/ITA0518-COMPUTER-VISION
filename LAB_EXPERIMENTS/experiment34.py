import cv2
import numpy as np

# Create a white image
image = np.ones((500, 500, 3), dtype=np.uint8) * 255

# Define circle properties
center = (250, 250)
radius = 100
color = (255, 0, 0)  # Blue color
thickness = 3

# Draw the circle
cv2.circle(image, center, radius, color, thickness)

# Display the image
cv2.imshow("White Image with Circle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the output image
cv2.imwrite("experiment34_output.jpg", image)
