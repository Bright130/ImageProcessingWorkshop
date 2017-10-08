# def do_operator(a, operator_fn):
#     return operator_fn(a)

# def increase(x):
#     return x+1

# print(do_operator(3, increase))
import numpy as np
import cv2

def conv2d(img,kernal):
    con = np.zeros(img.shape,dtype=np.uint8)
    imgh,imgw,a = img.shape
    kerh,kerw = kernal.shape
    anchorx,anchory = kerh//2 , kerw//2
    for x in range(0-kerw + imgw +1):
        for y in range(0-kerh + imgh +1):
            value = (img[y:y+kerh,x:x+kerw]*kernal).sum()
            if value>255:
                value = 255
            if value<0:
                value =0
            con[y+anchory,x+anchorx] = value

    return con

img = cv2.imread("x.jpg")
img2 = img.mean(axis=2).astype(np.uint8) # third axis

kernal = np.array([[-1.,-2.,-1.],[0.,0.,0.],[1.,2.,1.]])

img2 = conv2d(img,kernal)
cv2.imshow('a',img2)
cv2.waitKey(0)

print(img.shape)