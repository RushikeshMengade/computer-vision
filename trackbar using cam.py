import cv2
import numpy as np
cap=cv2.VideoCapture(0)
def nothing(s):
    pass

cv2.namedWindow("Track")

cv2.createTrackbar("L - H", "Track", 0, 179, nothing)
cv2.createTrackbar("L - S", "Track", 0, 255, nothing)
cv2.createTrackbar("L - V", "Track", 0, 255, nothing)
cv2.createTrackbar("U - H", "Track", 179, 179, nothing)
cv2.createTrackbar("U - S", "Track", 255, 255, nothing)
cv2.createTrackbar("U - V", "Track", 255, 255, nothing)

while True:
    _, frame = cap.read()
    frame=cv2.resize(frame,(200,200))
    #frame=cv2.imread("C:\\Users\\RUSHIKESH\\Pictures\\Saved Pictures\\lambo.jpg")
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    l_h = cv2.getTrackbarPos("L - H", "Track")
    l_s = cv2.getTrackbarPos("L - S", "Track")
    l_v = cv2.getTrackbarPos("L - V", "Track")
    u_h = cv2.getTrackbarPos("U - H", "Track")
    u_s = cv2.getTrackbarPos("U - S", "Track")
    u_v = cv2.getTrackbarPos("U - V", "Track")

    lower_blue = np.array([l_h, l_s, l_v])
    upper_blue = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask = cv2.resize(mask, (200, 200))
    result = cv2.bitwise_and(frame, frame, mask=mask)
    result = cv2.resize(result, (200, 200))
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)
    if cv2.waitKey(1) == ord("q"):
        cv2.destroyAllWindows()