import cv2
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    rev = cv2.flip(frame, 1)
    rev = cv2.rectangle(rev, (0, 255), (510, 128), (147, 96, 44), 5)
    font = cv2.FONT_HERSHEY_SIMPLEX
    rev = cv2.putText(rev, "Web Cam", (0, 128), font, 4,
                      (255, 255, 255), 10, cv2.LINE_AA)
    cv2.imshow('frame', rev)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()