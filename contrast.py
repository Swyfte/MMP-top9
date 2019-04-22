import cv2
import numpy as np
import csvEdit
import imutils
import Submodules as sb

mypath = "D:\Arianwen\Documents\GitHub\MMP-top9"
filename = ""
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and (".jpg" in f))]

for f in onlyfiles:
	filename = f
	img = cv2.imread(filename)
	height, width, colour = img.shape
	if width > 1000 or height > 1000:
		scaling = True
		if width > height:
			scaleBy = 1000/width
		else:
			scaleBy = 1000/height
	else:
		scaleBy = 1
	dim = (int(width * scaleBy), int(height * scaleBy))

	bckg = cv2.smooth(img, cv2.CV_BLUR, (5,5))
	contrast = 0

	for y in range(height):
		for x in range(width):
			if bckg[y,x] != 0:
				contrast += (img[y,x,0]-bckg[y,x])/bckg[y,x]

	contrast