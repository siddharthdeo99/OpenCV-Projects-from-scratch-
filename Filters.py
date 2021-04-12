import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
print(kernel)
path="mypic.jpg"
img=cv2.imread(path)
img=cv2.resize(img,(500,500))
iGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# iGary=cv2.resize(iGray,(50,50))
imgBlur=cv2.GaussianBlur(iGray,(15,15),0)
imgCanny=cv2.Canny(imgBlur,50,50)
imgDilation = cv2.dilate(imgCanny,kernel,iterations=1)
imgErode = cv2.erode(imgDilation,kernel,iterations=1)

cv2.imshow("Grey image",iGray)
cv2.imshow("Blur",imgBlur)
cv2.imshow("Canny",imgCanny)
cv2.imshow("imgDilation",imgDilation)
cv2.imshow("imgErode",imgErode)
cv2.waitKey(0)
