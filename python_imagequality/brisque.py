# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 16:35:16 2022

@author: Nava
"""
from brisque import BRISQUE
# Blind/Referenceless Image Spatial Quality Evaluator


# import PIL.Image
path = 'E:/payannameh/images/10.jpg'
photo = PIL.Image.open(path)
obj = BRISQUE()
print(obj.score(photo))