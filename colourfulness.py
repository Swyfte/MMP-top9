import cv2
import numpy as np
import imutils
import Submodules as sb

mypath = "D:\Arianwen\Documents\GitHub\MMP-top9"
filename = ""
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and (".jpg" in f))]

csvHeader = ["Filename","Colourfulness"]
csvName = "colourfulnessTest"

sb.csvWriteRow(csvName,csvHeader)

for f in onlyfiles:
	filename = f
	img = cv2.imread(filename)
	isGood = False
	#dim = sb.setScaling(img)
	b,g,r = sb.split(img)
	redgreen = np.absolute(r-g)
	yellowblue = np.absolute(0.5*(r+g)-b)
	rbMean = np.mean(redgreen)
	ybMean = np.mean(yellowblue)
	rbStd = np.std(redgreen)
	ybStd = np.std(yellowblue)

	stdRoot = np.sqrt((rbStd**2)+(ybStd**2))
	meanRoot = np.sqrt((rbMean**2)+(ybMean**2))

	colourful = stdRoot+(0.3*meanRoot)
	#80<x<120?
	if (colourful > 120) or (colourful < 80):
		isGood = True

	datum = [filename, colourful, isGood]
	sb.csvWriteRow(csvName,datum)

	"""# show the image
	cv2.putText(img, "{:.2f}".format(colourful), (10, 60),
		cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
	imgSml = cv2.resize(img, dim)
	cv2.imshow(filename, imgSml)
	cv2.waitKey(0)"""