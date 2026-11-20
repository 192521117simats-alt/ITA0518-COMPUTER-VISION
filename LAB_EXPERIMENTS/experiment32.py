import cv2
import numpy as np
# Create a white image
height, width = 500, 500
image = np.ones((height, width, 3), dtype=np.uint8) * 255
# Box dimensions: one-tenth of image height and width
box_h = height // 10
box_w = width // 10
# Draw black box in the top-left corner
image[0:box_h, 0:box_w] = (0, 0, 0)
# Draw blue box in the top-right corner
image[0:box_h, width-box_w:width] = (255, 0, 0)
# Draw green box in the bottom-left corner
image[height-box_h:height, 0:box_w] = (0, 255, 0)
# Draw red box in the bottom-right corner
image[height-box_h:height, width-box_w:width] = (0, 0, 255)
# Display the image
cv2.imshow("Colored Corner Boxes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Save the image
cv2.imwrite("experiment32_output.jpg", image)
