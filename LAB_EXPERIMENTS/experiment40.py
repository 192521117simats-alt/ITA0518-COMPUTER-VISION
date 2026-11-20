import cv2
import pytesseract

# Set the Tesseract executable path for Windows
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Open the input video
cap = cv2.VideoCapture("video.mp4")

if not cap.isOpened():
    print("Error: Cannot open video.mp4")
    exit()

# Process video frames
while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Extract text using OCR
    text = pytesseract.image_to_string(gray)

    # Print detected text
    if text.strip():
        print("Extracted Text:")
        print(text)

    # Display video frame
    cv2.imshow("Text Extraction from Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

