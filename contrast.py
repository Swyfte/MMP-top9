import cv2
import numpy as np
import imutils
import Submodules as sb
import scipy.stats as stats

mypath = "D:\Arianwen\Documents\GitHub\MMP-top9"
filename = ""
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and (".jpg" in f))]

for f in onlyfiles:
	filename = f
	img = cv2.imread(filename)
	height, width, colour = img.shape
	
	dim = sb.setScaling(img)

	#grey = sb.grey(img)

	#hist_img = cv2.calcHist([grey],[0],None,[256],[0,256])
	#contrast = stats.entropy(hist_img)

	imgLAB = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
	bckg = cv2.blur(imgLAB,(5,5))
	contrast = 0

	for y in range(height):
		for x in range(width):
			if bckg[y,x].any() != 0:
				contrast += (img[y,x,0]-bckg[y,x])/bckg[y,x]

	contrast /= (height*width)



	cv2.putText(img, str(contrast), (10, 60),
		cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
	imgSml = cv2.resize(img, dim)
	cv2.imshow(filename, imgSml)
	cv2.waitKey(0)