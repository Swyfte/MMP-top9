import cv2
import numpy as np
from matplotlib import pyplot as plt
import random
import math
import Submodules as sb
import vanishing_point as vp
from itertools import starmap

mypath = "D:\Arianwen\Documents\GitHub\MMP-top9"
filename = ""
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and ("centre_" not in f) and (".jpg" in f))]

for f in onlyfiles:
	filename = f
	img = cv2.imread(filename)
	height, width, colour = img.shape
	percent = 25
	dim = (int(width * percent/100), int(height * percent/100))
	kernel = np.ones((15,15), np.uint8)

	blur = cv2.GaussianBlur(img,(5,5),0)
	opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
	edges = cv2.Canny(opening,50,150,apertureSize = 3)
	lines = cv2.HoughLines(edges, 1, np.pi/180, 300)
	hough_lines = []
	if lines is not None:
		for line in lines:
			hough_lines.extend(list(starmap(vp.endpoints, line)))

	if len(lines) > 0:
		intersect = vp.find_intersections(hough_lines)
		if intersect:
			new_img = img.copy()
			grid_size = min(height, width) // 3
			vanishpoint = vp.find_vanishing_point(new_img, grid_size, intersect)
			savename = "centre_" + filename
			saveLoc = join(mypath, savename)
			cv2.imwrite(saveLoc, new_img)