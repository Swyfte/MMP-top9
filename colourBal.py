import cv2
import numpy as np
from matplotlib import pyplot as plt

mypath = "D:\Arianwen\Documents\GitHub\MMP-top9"
filename = ""
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and (".jpg" in f))]

for f in onlyfiles:
	filename = f
	img = cv2.imread(filename) 
	height, width, colour = img.shape
	Size = height*width
	hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	
	hueImg = img[:,:,0]
	satImg = img[:,:,1]
	valImg = img[:,:,2]
	cv2.imshow("Hue", hueImg)
	cv2.imshow("Saturation", satImg)
	cv2.imshow("Value", valImg)
	cv2.waitKey(0)