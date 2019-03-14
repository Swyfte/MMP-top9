import cv2
import numpy as np
from matplotlib import pyplot as plt

## get a list of files in the directory ideally just jpgs

mypath = "E:/MMP files/"
filename = ""

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and (".jpg" in f) and ("gray_" in f) and ("thresh_" not in f))]


## https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory

## loop through the list "for filename in listname:"
for f in onlyfiles:
	filename = f
	## modify so this reads "filename" not test.jpg
	img = cv2.imread(filename) 
	ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
	## (filename being the original filename) using string concatenation
	filename = "thresh_" + filename
	## save the image out to the new filename
	saveLoc = join(mypath, filename)
	cv2.imwrite(saveLoc, thresh)
## end of loop/program
