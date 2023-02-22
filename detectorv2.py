import cv2
import numpy as np
img = cv2.imread('edgedetection/cardgiannis.jpeg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

minLineLength = 100 #img.shape[1] - 300
lines = cv2.HoughLinesP(image=edges, rho=0.02, theta=np.pi / 500,     threshold=10, lines=np.array([]), minLineLength=minLineLength, maxLineGap=2)
a, b, c = lines.shape

for i in range(a):
    cv2.line(img, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2],  lines[i][0][3]), (0, 0, 255), 2, cv2.LINE_AA)
cv2.imshow('lines', img)
cv2.waitKey()