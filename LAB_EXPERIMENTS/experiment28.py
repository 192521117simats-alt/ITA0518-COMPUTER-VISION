import cv2
# Read the video
video = cv2.VideoCapture("video1.mp4")
# Load the vehicle detection classifier
cascade_path = cv2.data.haarcascades + "haarcascade_car.xml"
vehicle_cascade = cv2.CascadeClassifier(cascade_path)
# Check classifier
if vehicle_cascade.empty():
    print("Error: Vehicle cascade file not found.")
    video.release()
    exit()
# Check video
if not video.isOpened():
    print("Error: Cannot open video.mp4")
    exit()
while True:
    ret, frame = video.read()
    if not ret:
        break
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect vehicles
    vehicles = vehicle_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(30, 30)
    )
    # Draw rectangles around detected vehicles
    for (x, y, w, h) in vehicles:
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )
    # Display vehicle count
    cv2.putText(
        frame,
        "Vehicles: " + str(len(vehicles)),
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )
    # Display output
    cv2.imshow("Vehicle Detection", frame)
    # Press Q to exit
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break
video.release()
cv2.destroyAllWindows()
