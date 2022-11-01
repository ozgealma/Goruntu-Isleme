import cv2
import numpy as np

deniz= cv2.imread("deniz.png",0)
cv2.imshow("deniz",deniz)
cv2.waitKey()

a= np.max(deniz)
print(a)

[h,w] = deniz.shape
yeniDeniz = np.zeros([h,w], dtype=np.uint8)
for i in range(h):
    for j in range(w):
        yeniDeniz[i,j] = a - deniz[i,j]


cv2.imshow("deniz",yeniDeniz)
cv2.waitKey()

