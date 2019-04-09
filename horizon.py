import cv2
import numpy as np
from matplotlib import pyplot as plt
import math
import Submodules as sb

mypath = "D:\Arianwen\Documents\GitHub\MMP-top9"
filename = ""
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and (".jpg" in f))]

kernel_sharpening = np.array([[-1,-1,-1], 
                              [-1, 9,-1],
                              [-1,-1,-1]])

## Loop through and 
for f in onlyfiles:
	filename = f
	img = cv2.imread(filename)
	height, width, colour = img.shape
	percent = 75
	dim = (int(width * percent/100), int(height * percent/100))
	#grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	#sharp = cv2.filter2D(grey, -1, kernel_sharpening)
	blur = cv2.GaussianBlur(img,(5,5),0)
	new_img = np.zeros(img.shape, img.dtype)
	new_img = cv2.convertScaleAbs(blur,alpha=2.0,beta=0)
	edges = cv2.Canny(new_img,200,250)
	#lines = cv2.HoughLinesP(edges,2,np.pi/2,200, None, int(width/4), 100)
	lines = cv2.HoughLines(edges, 2, np.pi/2, 200, 100, 200)
	imgSML = cv2.resize(img, dim)
	edgesSML = cv2.resize(edges, dim)
	cv2.imshow("edges",edgesSML)
	cv2.imshow("img", imgSML)
	##Remove code. Borrowed for testing.
	for line in lines:
		for rho,theta in line:
			a = np.cos(theta)
			b = np.sin(theta)
			x0 = a*rho
			y0 = b*rho
			x1 = int(x0 + 1000*(-b))
			y1 = int(y0 + 1000*(a))
			x2 = int(x0 - 1000*(-b))
			y2 = int(y0 - 1000*(a))
			if (x1 != x2):
				cv2.line(edges,(x1,y1),(x2,y2),(255,255,0),2)
	"""if lines is not None:
		for i in range(0, len(lines)):
			l = lines[i][0]
			cv2.line(img, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv2.LINE_AA)"""
	edgeshowSML = cv2.resize(edges, dim)
	cv2.imshow("Detected Lines (in red) - Standard Hough Line Transform", edgeshowSML)
	###
	cv2.waitKey(0)