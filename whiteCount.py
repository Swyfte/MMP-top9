import cv2
import numpy as np
from matplotlib import pyplot as plt

## get a list of files in the directory ideally just jpgs

mypath = "E:/MMP files/"
filename = ""

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and (".jpg" in f) and ("thresh_" in f))]


## https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory

## loop through the list "for filename in listname:"
for f in onlyfiles:
	blackCount = 0
	whiteCount = 0
	filename = f
	## modify so this reads "filename" not test.jpg
	img = cv2.imread(filename,0)
	height, width = img.shape
	Size = img.size
	print()

	print(filename)
	print("size " + str(Size))
	whiteCount = cv2.countNonZero(img)
	print("w/c " + str(whiteCount))
	blackCount = Size - whiteCount
	print("b/c " + str(blackCount))
	if float(whiteCount)/Size > 0.5:
		print("white, " + str(round((float(whiteCount)/Size)*100, 2)) + "% white")
	else:
		print("black, " + str(round((float(whiteCount)/Size)*100, 2)) + "% white")
	print("height and width :", height, width)
## end of loop/program
