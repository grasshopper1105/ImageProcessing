import cv2

cap = cv2.VideoCapture(0)
fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()
se = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

while cap.isOpened():
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    _, binary = cv2.threshold(fgmask, 215, 255, cv2.THRESH_TRIANGLE)
    binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, se)
    res = cv2.bitwise_and(frame, frame, mask=binary)
    cv2.imshow("res", res)

    if cv2.waitKey(1000 // 12) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()