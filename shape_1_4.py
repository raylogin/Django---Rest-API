import numpy
import cv2
  
img = numpy.zeros((400, 400, 3), dtype = "uint8")
line = [(59, 110),(341, 100),(350, 109),(328, 161),(323, 179),(229, 213),(83, 187),(211, 213),(50, 119),(78, 171)]
circle = [(50, 110), (350, 100), (325, 170), (75, 180),  (220, 220)]
for x in range(5):
    cv2.line(img, line[x*2],line[(x*2)+1],(255, 0, 0), 2)
    cv2.circle(img,circle[x], 11, (0, 0, 255), 3)

cv2.imshow('dark', img)
  
cv2.waitKey(0)
cv2.destroyAllWindows()