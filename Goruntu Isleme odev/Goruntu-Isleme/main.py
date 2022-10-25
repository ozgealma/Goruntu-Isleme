import cv2
import numpy as np

maymun= cv2.imread("maymun.png",0)
cv2.imshow("resim",maymun)
cv2.waitKey()


diziBoyut = 256
diziAralık = (0, 256)

Hist = np.zeros(256)
a,b = maymun.shape

for u in range(0,a):
    for v in range(0, b):
        deger = maymun[u,v]
        Hist[deger] = deger + 1