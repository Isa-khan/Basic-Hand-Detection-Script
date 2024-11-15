import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(1)
cap.set(3, 1280)  
cap.set(4, 720)   


detector = HandDetector(detectionCon=1, maxHands=2) 

while True:
    success, img = cap.read()  
    if not success:
        break

    img = detector.findHands(img)  
    cv2.imshow("Smart Camera", img)  

    if cv2.waitKey(1) == ord("q"):  
        break
    

cap.release()
cv2.destroyAllWindows()
