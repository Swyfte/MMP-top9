import cv2
import numpy as np
from matplotlib import pyplot as plt

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
	percent = 25
	dim = (int(width * percent/100), int(height * percent/100))
	sharp = cv2.filter2D(img, -1, kernel_sharpening)
	edges = cv2.Canny(sharp,225,250)
	imgSML = cv2.resize(img, dim)
	edgesSML = cv2.resize(edges, dim)
	cv2.imshow("edges",edgesSML)
	cv2.imshow("img", imgSML)
	cv2.waitKey(0)
	