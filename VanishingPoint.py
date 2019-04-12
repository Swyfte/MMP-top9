import cv2
import numpy as np
from matplotlib import pyplot as plt
import random
import math
import Submodules as sb

def det(a, b):
    return a[0] * b[1] - a[1] * b[0]

def line_intersection(line1, line2):
    x_diff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    y_diff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    div = det(x_diff, y_diff)
    if div == 0:
        return None  # Lines don't cross

    d = (det(*line1), det(*line2))
    x = det(d, x_diff) / div
    y = det(d, y_diff) / div

    return x, y

mypath = "D:\Arianwen\Documents\GitHub\MMP-top9"
filename = ""
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and (".jpg" in f))]

for f in onlyfiles:
	filename = f
	img = cv2.imread(filename)
	height, width, colour = img.shape
	percent = 25
	dim = (int(width * percent/100), int(height * percent/100))
	kernel = np.ones((15,15), np.uint8)
	size = 100

	blur = cv2.GaussianBlur(img,(5,5),0)
	opening = cv2.morphologyEx(blur, cv2.MORPH_OPEN, kernel)
	edges = cv2.Canny(opening,50,150,apertureSize = 3)
	lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

	if lines:
		if len(lines) > size:
			size = len(lines)
		sampleLines = random.sample(lines, size)

	

	imgSML = cv2.resize(img, dim)
	edgesSML = cv2.resize(edges, dim)
	cv2.imshow("edges",edgesSML)
	cv2.imshow("img", imgSML)

	for line in lines:
		for rho,theta in line:
			a = np.cos(theta)
			b = np.sin(theta)
			x0 = a*rho
			y0 = b*rho
			x1 = int(x0 + 5000*(-b))
			y1 = int(y0 + 5000*(a))
			x2 = int(x0 - 5000*(-b))
			y2 = int(y0 - 5000*(a))
			cv2.line(img,(x1,y1),(x2,y2),(255,255,0),2)
	edgeshowSML = cv2.resize(img, dim)
	cv2.imshow("Detected Lines (in red) - Standard Hough Line Transform", edgeshowSML)
	cv2.waitKey(0)