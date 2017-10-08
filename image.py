# def do_operator(a, operator_fn):
#     return operator_fn(a)

# def increase(x):
#     return x+1

# print(do_operator(3, increase))
import numpy as np
import cv2

def conv2d(img,kernal):
    con = np.zeros(img.shape,dtype=np.uint8)
    imgh,imgw,imgc = img.shape
    kerh,kerw,imgc = kernal.shape
    anchorx,anchory = kerh//2 , kerw//2
    for c in range(imgc):
        for x in range(0-kerw + imgw +1):
            for y in range(0-kerh + imgh +1):
                value = (img[y:y+kerh,x:x+kerw,c]*kernal).sum()
                if value>255:
                    value = 255 #offset
                if value<0:
                    value =0
                con[y+anchory,x+anchorx,c] = value

    return con

def colorwhite(img):
    con = np.zeros(img.shape,dtype=np.uint8)
    imgh,imgw,imgc = img.shape

    for x in range(imgw-39):
        for y in range(imgh-39):
            value = (img[y:y+40,x:x+40,2]).sum()+(img[y:y+40,x:x+40,0]).sum()+(img[y:y+40,x:x+40,1]).sum()
            if value<5500*3:
                value = 255
                con[y+20,x+20,0] = value
                con[y+20,x+20,1] = value
                con[y+20,x+20,2] = value
            else:
                con[y+20,x+20,0] = img[y+20,x+20,0]
                con[y+20,x+20,1] = img[y+20,x+20,1]
                con[y+20,x+20,2] = img[y+20,x+20,2] 
            
    return con

img = cv2.imread("x.jpg")
#img2 = img.mean(axis=2).astype(np.uint8) # black-white img in third axis

kernal = np.array([
                  [[-1.,-2.,-1.],[0.,0.,0.],[1.,2.,1.]],
                  [[-1.,-2.,-1.],[0.,0.,0.],[1.,2.,1.]],
                  [[-1.,-2.,-1.],[0.,0.,0.],[1.,2.,1.]]
                  ])

img2 = conv2d(img,kernal)

#blur it with this kernal
kernal = np.array([
                  [[1/27,1/27,1/27],[1/27,1/27,1/27],[1/27,1/27,1/27]],
                  [[1/27,1/27,1/27],[1/27,1/27,1/27],[1/27,1/27,1/27]],
                  [[1/27,1/27,1/27],[1/27,1/27,1/27],[1/27,1/27,1/27]]
                  ])
img3 = conv2d(img2,kernal)

#kernal = np.array([[-1.,0.,1.],[-2.,0.,2.],[-1.,0.,1.]])
#img3+= cv2.filter2D(img,-1,kernal)
#img2 = cv2.filter2D(img,-1,kernal)
#kernal = np.array([[-1.,0.,1.],[-2.,0.,2.],[-1.,0.,1.]])
#img3 = cv2.filter2D(img,-1,kernal)
#img4= img2+img3

img4 = colorwhite(img3)
cv2.imshow('a',img)
cv2.imshow('b',img3)
cv2.imshow('c',img4)
cv2.waitKey(0)

print(img.shape)