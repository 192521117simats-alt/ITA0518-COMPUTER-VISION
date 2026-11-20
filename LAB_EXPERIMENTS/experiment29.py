import cv2
# Read the image
image = cv2.imread("image1.png")
if image is None:
    print("Error: Cannot load image1.png")
    exit()
# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Load eye detection classifier
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)
if eye_cascade.empty():
    print("Error: Eye cascade file not found")
    exit()
# Detect eyes
eyes = eye_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(20, 20)
)
# Draw rectangles around detected eyes
for (x, y, w, h) in eyes:
    cv2.rectangle(
        image,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )
# Display number of eyes detected
print("Number of eyes detected:", len(eyes))
# Display output image
cv2.imshow("Eye Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
