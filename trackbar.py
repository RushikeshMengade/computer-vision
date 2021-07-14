import cv2
import numpy as np
def empty(s):
    pass


cv2.namedWindow("Track")
cv2.createTrackbar("Hue min", "Track", 0, 179, empty)
cv2.createTrackbar("Hue Max", "Track", 179, 179, empty)
cv2.createTrackbar("Sat Min", "Track", 0, 255, empty)
cv2.createTrackbar("Sat Max", "Track", 255, 255, empty)
cv2.createTrackbar("Val Min", "Track", 0, 255, empty)
cv2.createTrackbar("Val Max", "Track", 255, 255, empty)

while True:
    img5 = cv2.imread("C:\\Users\\RUSHIKESH\\Pictures\\Saved Pictures\\lambo.jpg")
    imghsv = cv2.cvtColor(img5, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "Track")
    h_max = cv2.getTrackbarPos("Hue Max", "Track")
    s_min = cv2.getTrackbarPos("Sat Min", "Track")
    s_max = cv2.getTrackbarPos("Sat Max", "Track")
    v_min = cv2.getTrackbarPos("Val Min", "Track")
    v_max = cv2.getTrackbarPos("Val Max", "Track")

    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imghsv,lower,upper)
    result=cv2.bitwise_and(img5,img5,mask=mask)

    cv2.imshow("img5",img5)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)
    if cv2.waitKey(1)  == ord("q"):
        cv2.destroyAllWindows()
        break
cv2.destroyAllWindows()
