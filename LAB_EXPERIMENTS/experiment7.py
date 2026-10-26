import cv2

# Open the video
video = cv2.VideoCapture("video.mp4")

# Check whether the video opened successfully
if not video.isOpened():
    print("Error: Could not open video")
    exit()

# ---------------- NORMAL MOTION ----------------
while True:
    ret, frame = video.read()

    if not ret:
        break

    cv2.imshow("Normal Motion", frame)

    # Press q to stop
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()


# ---------------- SLOW MOTION ----------------
video = cv2.VideoCapture("video.mp4")

while True:
    ret, frame = video.read()

    if not ret:
        break

    cv2.imshow("Slow Motion", frame)

    # Larger delay = slow motion
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()


# ---------------- FAST MOTION ----------------
video = cv2.VideoCapture("video.mp4")

while True:
    ret, frame = video.read()

    if not ret:
        break

    cv2.imshow("Fast Motion", frame)

    # Smaller delay = fast motion
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
