import cv2
import numpy as np

img=cv2.imread('image.jpeg', cv2.IMREAD_COLOR)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

b=img[:,:,0]
g=img[:,:,1]
r=img[:,:,2]


cv2.imshow('Blue channel', b)
cv2.imshow('Green channel', g)
cv2.imshow('Red channel', r)

yeniresim=np.clip(img,0,255)
yeniresim=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
yeniresim[:,:,0]=g
yeniresim[:,:,1]=r
yeniresim[:,:,2]=b


cv2.imshow('New Image', yeniresim)

cv2.waitKey(0)
