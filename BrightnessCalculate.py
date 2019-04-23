import cv2
import numpy as np
from matplotlib import pyplot as plt
import Submodules as sb


## Import the jpg files
mypath = "D:\Arianwen\Documents\GitHub\MMP-top9"
filename = ""

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and (".jpg" in f) and ("gray_" not in f))]

## Loop through and make each image greyscale, then thresholded, then count the white
for f in onlyfiles:
	filename = f
	img = cv2.imread(filename)
	grey = sb.grey(img)
	ret,thresh = sb.thresh(grey)
	sb.whiteCountTest(thresh,filename)
