import cv2
import numpy as np

img = "card.jpg"
width,height=250,350
i=cv2.imread(img)
i=cv2.resize(i,(400,400),cv2.FILLED)
# cv2.imshow("img",i)
# cv2.imwrite("sisi.jpg",i)
pts1=np.float32([[253,178],[381,233],[114,281],[245,353]])#Dimmension of pixel (open msPaint and check that value)
print(pts1)
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgOutput=cv2.warpPerspective(i,matrix,(width,height),cv2.FILLED)

for dot in range(0,4):
    cv2.circle(i, (pts1[dot][0], pts1[dot][1]), 3, (0, 0, 255), cv2.FILLED)

cv2.imshow("img",i)
cv2.imshow("Image",imgOutput)
cv2.waitKey(0)
