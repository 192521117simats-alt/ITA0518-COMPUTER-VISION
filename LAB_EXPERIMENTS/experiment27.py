
import cv2

# Read the input image
image = cv2.imread("image.jpg")

# Check whether the image is loaded
if image is None:
    print("Error: Could not load image")
    exit()

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load the pre-trained face detection classifier
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Check whether the classifier is loaded
if face_cascade.empty():
    print("Error: Could not load face detection model")
    exit()

# Detect faces
faces = face_cascade.detectMultiScale(
    gray_image,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(
        image,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

# Display the result
cv2.imshow("Experiment 27 - Face Detection", image)

print("Number of faces detected:", len(faces))

# Wait until a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
