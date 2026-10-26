
import cv2

# Open the input video
cap = cv2.VideoCapture("video.mp4")

if not cap.isOpened():
    print("Error: Could not open video")
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

# Get video properties from the first frame
height, width = frames[0].shape[:2]

# Set output video properties
fps = 25

# Create output video
output = cv2.VideoWriter(
    "reversed_video.mp4",
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (width, height)
)

# Save frames in reverse order
for frame in reversed(frames):
    output.write(frame)

output.release()

print("Reversed video saved successfully!")

# Open the reversed video
reverse_cap = cv2.VideoCapture("reversed_video.mp4")

# Play the reversed video
while reverse_cap.isOpened():
    ret, frame = reverse_cap.read()

    if not ret:
        break

    cv2.imshow("Experiment 26 - Reversed Video", frame)

    # Press Q to stop playback
    if cv2.waitKey(40) & 0xFF == ord("q"):
        break

reverse_cap.release()
cv2.destroyAllWindows()

print("Video playback completed.")
