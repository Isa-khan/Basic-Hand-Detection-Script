import cv2
from cvzone.HandTrackingModule import HandDetector

# Initialize the webcam
cap = cv2.VideoCapture(1)
cap.set(3, 1280)  # Set width
cap.set(4, 720)   # Set height

# Initialize the hand detector
detector = HandDetector(detectionCon=1, maxHands=2) # was 0.6

while True:
    success, img = cap.read()  # Capture frames from the webcam
    if not success:
        break

    img = detector.findHands(img)  # Detect hands in the frame
    cv2.imshow("Smart Camera", img)  # Display the frame with hand detection

    if cv2.waitKey(1) == ord("q"):  # Exit if 'q' is pressed
        break

cap.release()
cv2.destroyAllWindows()
