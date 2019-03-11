import cv2
import numpy as np
from matplotlib import pyplot as plt

mypath = "D:\Arianwen\Documents\GitHub\MMP-top9"
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
	grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	leftSide = grey[:, :half]
	cv2.imshow("cropped", leftSide)
	cv2.waitKey(0)
	mirror = cv2.flip(leftSide, 1)
	cv2.imshow("flipped", mirror)
	cv2.waitKey(0)
	rightSide = grey[:, half:]
	cv2.imshow("right", rightSide)
	cv2.waitKey(0)

	compared = cv2.bitwise_and(mirror, rightSide)
	cv2.imshow("compared", compared)
	cv2.waitKey(0)