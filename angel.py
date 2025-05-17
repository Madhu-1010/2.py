import cv2
img=cv2.imread("sathu.jpeg")
_,global_threshold=cv2.threshold(img,120,255,cv2.THRESH_BINARY)
cv2.imshow("sathu.jpeg",global_threshold)
cv2.waitKey(20000)