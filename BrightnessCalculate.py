import cv2
import numpy as np
from matplotlib import pyplot as plt

## Import the jpg files
mypath = "D:\Arianwen\Documents\GitHub\MMP-top9"
filename = ""
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and (".jpg" in f) and ("gray_" not in f))]

## Loop through and make each image greyscale, then thresholded, then count the white
for f in onlyfiles:
	filename = f
	img = cv2.imread(filename) 
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert it to grey 
	ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY) #threshold that lad
	#The following chunk calculates the white balance
	height, width, colour = img.shape
	Size = thresh.size
	print()
	print(filename)
	#print("size " + str(Size))
	whiteCount = cv2.countNonZero(thresh)
	#print("w/c " + str(whiteCount))
	blackCount = Size - whiteCount
	#print("b/c " + str(blackCount))
	if float(whiteCount)/Size > 0.5:
		print("Light, " + str(round((float(whiteCount)/Size)*100, 2)) + "% white")
	else:
		print("Dark, " + str(round((float(whiteCount)/Size)*100, 2)) + "% white")
	print("height and width :", height, width)
