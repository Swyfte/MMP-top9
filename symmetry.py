import cv2
import numpy as np
from matplotlib import pyplot as plt

mypath = "E:/MMP files/"
filename = ""
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and (".jpg" in f))]

## Loop through and find half of each image, flip it, then compare the two halves
for f in onlyfiles:
	filename = f
	img = cv2.imread(filename) 
	height, width, colour = img.shape
	half = int(width/2)
	leftSide = img[:, :half]
	cv2.imshow("cropped", leftSide)
	cv2.waitKey(0)
	mirror = cv2.flip(leftSide, 1)
	cv2.imshow("flipped", mirror)
	cv2.waitKey(0)
	