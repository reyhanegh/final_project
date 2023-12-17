# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 11:07:58 2022

@author: Nava
"""
import imquality.brisque as brisque
import PIL.Image
path = 'E:/payannameh/images/4.jpg'
photo = PIL.Image.open(path)
print(brisque.score(photo))


# import cv2
# import numpy as np


# img = cv2.imread(path)[:,:,:3]

# # cv2.imshow('image',img)
# # cv2.waitKey(0)


# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# img2 = np.zeros_like(img)
# img2[:,:,0] = gray
# img2[:,:,1] = gray
# img2[:,:,2] = gray
# # # cv2.imwrite('10524.jpg', img2)


# print(brisque.score(img))
