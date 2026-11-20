import cv2
# Read the image
image = cv2.imread("image2.jpg")
if image is None:
    print("Error: Cannot load image2.jpg")
    exit()
# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Load face detection classifier
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
# Load smile detection classifier
smile_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_smile.xml"
)
if face_cascade.empty() or smile_cascade.empty():
    print("Error: Cascade file could not be loaded")
    exit()
# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)
smile_count = 0
# Detect smiles inside each face
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    face_gray = gray[y:y + h, x:x + w]
    face_color = image[y:y + h, x:x + w]
    smiles = smile_cascade.detectMultiScale(
        face_gray,
        scaleFactor=1.7,
        minNeighbors=20,
        minSize=(20, 20)
    )
    if len(smiles) > 0:
        smile_count += 1
    for (sx, sy, sw, sh) in smiles:
        cv2.rectangle(
            face_color,
            (sx, sy),
            (sx + sw, sy + sh),
            (0, 255, 0),
            2
        )
# Display result
print("Number of faces detected:", len(faces))
print("Number of smiling faces detected:", smile_count)
cv2.imshow("Smile Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
