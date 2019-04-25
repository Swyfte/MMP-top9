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
	dim = sb.setScaling(img)
	blur = cv2.GaussianBlur(img,(5,5),0)
	new_img = np.zeros(img.shape, img.dtype)
	new_img = cv2.convertScaleAbs(blur,alpha=2.0,beta=0)
	edges = cv2.Canny(cv2.resize(cv2.split(img)[0], (width / 4, height / 4), 0, 0, cv2.INTER_NEAREST),
            200, 600, apertureSize=3)
	lines = cv2.HoughLines(edges, 2, np.pi/2, 200, 100, 200)
	edgesSML = cv2.resize(edges, dim)
	cv2.imshow("edges",edgesSML)
	##Remove code. Borrowed for testing.
	##When plotting lines, add highest line to a storing variable?
	##Doesn't detect horizons for daytime seas....
	for line in lines:
		for rho,theta in line:
			a = np.cos(theta)
			b = np.sin(theta)
			x0 = a*rho
			y0 = b*rho
			x1 = int(x0 + width*(-b))
			y1 = int(y0 + 1000*(a))
			x2 = int(x0 - width*(-b))
			y2 = int(y0 - 1000*(a))
			if (x1 != x2):
				cv2.line(img,(x1,y1),(x2,y2),(255,255,0),2)
	edgeshowSML = cv2.resize(img, dim)
	cv2.imshow("Detected Lines (in red) - Standard Hough Line Transform", edgeshowSML)
	###
	cv2.waitKey(0)