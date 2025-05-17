import cv2
import numpy as np
image=cv2.imread("princess.jpg")
image=cv2.resize(image,(600,400))
gaussian_blur=cv2.GaussianBlur(image,(5,5),0)
median_blur=cv2.medianBlur(image,5)
bilateral_blur=cv2.bilateralFilter(image,9,75,75)
cv2.imshow("Original Image",image)
cv2.imshow("Gaussian Blur",gaussian_blur)
cv2.imshow("Median Blur",median_blur)
cv2.imshow("Bilateral Filtering",bilateral_blur)
cv2.waitKey(10000)
cv2.destroyAllWindows()