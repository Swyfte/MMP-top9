import cv2
import numpy as np
import imutils
import Submodules as sb
import scipy.stats as stats
from matplotlib import pyplot as plt
from imutils import build_montages

mypath = "D:\Arianwen\Documents\GitHub\MMP-top9"
filename = ""
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and (".jpg" in f))]

images = []
datum = ("filename", "Contrast","Brightness","Accepted")
csvName = "contrastTest"
sb.csvWriteRow(csvName,datum)

for f in onlyfiles:
	filename = f
	img = cv2.imread(filename)
	height, width, colour = img.shape
	dim = sb.setScaling(img)

	space_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

	hist_img = cv2.calcHist([space_img[0]],[0],None,[256],[0,256])
	contrast = stats.variation(hist_img,None)

	grey = sb.grey(img)
	ret, thresh = sb.thresh(grey)
	wcount = sb.whiteCount(thresh)

	accepted = True

	if (contrast-(10*wcount) < 0.1) or (wcount < 0.1):
		accepted = False
	
	datum = (filename, contrast, (wcount*100), accepted)
	sb.csvWriteRow(csvName,datum)