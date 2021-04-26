import cv2

path="mypic.jpg"
img=cv2.imread(path)
print(img.shape)
w,h=400,400
imgResize=cv2.resize(img,(w,h))
cv2.imshow("img resize",imgResize)
print(imgResize.shape)
imgCrop=img[200:700,350:800]
#resize crop image to original size
# imgCropResize=cv2.resize(imgCrop,(1242,1079))
imgCropResize=cv2.resize(imgCrop,(img.shape[1],img.shape[0]))

cv2.imshow("img crop",imgCrop)
cv2.imshow("img crop resize",imgCropResize)

cv2.waitKey(0)
