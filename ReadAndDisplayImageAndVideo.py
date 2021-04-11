import cv2
frameWidth = 720
frameHeigh = 480

cap= cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeigh)

# cap= cv2.VideoCapture("D:\movie\python meet (2021-03-06 at 05-17 GMT-8) - Google Drive_2.mp4")

while True:
    success,img= cap.read()
#     img = cv2.resize(img,(frameWidth,frameHeigh))
    #cv2.resize is for resize a video. For Resizing a webcam use variable.set() fn
    cv2.imshow("MyVIDEO",img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
#Above code is for video, below one is for image
# img = cv2.imread("mypic.jpg")
# img=cv2.resize(img,(720,110))
# cv2.imshow("My PIC",img)
# cv2.waitKey(0)


