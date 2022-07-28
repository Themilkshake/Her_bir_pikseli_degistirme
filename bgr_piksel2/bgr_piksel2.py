import cv2
import numpy as np

#hangi sayısal değerde olduğunu okudu.
resiim = cv2.imread("joker.jpg")

"""
Resmin her bir pikselin sayısal değerini(rengini) değiştiriyor.

 *Resim[i:j]  ---> resmin i kısmı 1'den 300'e kadar sırayla çoğalıyor.
 
 *Resim[i:j]  ---> resmin j kısmı 1'den 500'e kadar sırayla artıyor 
 ve hepsine teker teker beyaz rengi ekliyor.
"""

for i in range(300):
    for j in range(500):
        resiim[i,j]=[255,255,255] #<-- beyaz renk (255, 255, 255)
    
cv2.imshow("Joker Resmi", resiim)



cv2.waitKey(0)
cv2.destroyAllWindows()
