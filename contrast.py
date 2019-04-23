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
datum = ("filename", "Contrast/Brightness")
sb.csvWriteRow(datum)

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
	
	contbright = contrast/(100*wcount)

	accepted = True

	if (contrast-(10*wcount) < 0.1) or (wcount < 0.1):
		accepted = False

	imgSml = cv2.resize(img, (400,300))
	cv2.putText(imgSml, str(contbright), (10, 60),
		cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
	cv2.putText(imgSml, str(wcount), (10, 120),
		cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
	cv2.putText(imgSml, str(accepted), (10, 180),
		cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
	images.append(imgSml)

montages = build_montages(images,(400,300), (4,3))
i = 0
for montage in montages:
	cv2.imshow("Montage " + str(i), montage)
	i += 1
cv2.waitKey(0)