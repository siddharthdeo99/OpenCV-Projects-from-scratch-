import cv2
import numpy as np

# img=np.zeros((512,512,3))
img=np.zeros((512,512,3),np.uint8)
#BGR -(bue,green,red)
#(rarnge-0-255)
img[:]=255,255,255

# cv2.line(img,(0,0),(100,100),(0,0,255),2)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(120,0,255),2)
# cv2.rectangle(img,(350,100),(450,200),(0,255,0),cv2.FILLED)
cv2.rectangle(img,(350,100),(450,200),(0,255,0),2)
# cv2.circle(img,(150,400),50,(255,0,0),5)
cv2.circle(img,(150,400),50,(255,0,0),cv2.FILLED)
cv2.putText(img,"Siddharth",(60,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,0,255),1)


print(img)
cv2.imshow("img",img)
cv2.waitKey(0)
