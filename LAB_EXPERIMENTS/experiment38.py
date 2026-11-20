import cv2

# Load the input image
image = cv2.imread("image1.png")

if image is None:
    print("Error: Cannot load image1.png")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load face detection classifier
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(
        image, (x, y), (x + w, y + h),
        (0, 255, 0), 2
    )

# Count the detected faces
count = len(faces)
print("Number of faces detected:", count)

# Display the result
cv2.imshow("Face Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the output
cv2.imwrite("experiment38_output.jpg", image)
