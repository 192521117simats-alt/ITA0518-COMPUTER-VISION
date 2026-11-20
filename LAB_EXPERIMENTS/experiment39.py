import cv2

# Open the input video
cap = cv2.VideoCapture("video.mp4")

if not cap.isOpened():
    print("Error: Cannot open video.mp4")
    exit()

# Read all video frames
frames = []

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frames.append(frame)

cap.release()

if len(frames) == 0:
    print("Error: No frames found")
    exit()

# Play frames in reverse and slow motion
print("Playing video in reverse slow motion. Press Q to quit.")

for frame in reversed(frames):
    cv2.imshow("Reverse Slow Motion Video", frame)

    # Larger delay makes playback slower
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
