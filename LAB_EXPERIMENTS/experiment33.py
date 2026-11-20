import cv2
import numpy as np

# Create a white image
image = np.ones((500, 500, 3), dtype=np.uint8) * 255

# Draw a rectangle
start_point = (100, 100)
end_point = (400, 300)
color = (0, 0, 255)  # Red color
thickness = 3

cv2.rectangle(
    image,
    start_point,
    end_point,
    color,
    thickness
)

# Display the image
cv2.imshow("White Image with Rectangle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

