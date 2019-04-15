import cv2
import numpy as np
from matplotlib import pyplot as plt

mypath = "D:\Arianwen\Documents\GitHub\MMP-top9"
filename = ""
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and (".jpg" in f))]

channels = [
	([000,000,127],[127,140,255]), #Red
	([000,127,000],[127,255,160]), #Grn
	([127,000,000],[255,127,127])  #Blu
]

## Loop through and find each colour channel, masking it and counting
for f in onlyfiles:
	filename = f
	img = cv2.imread(filename) 
	height, width, colour = img.shape
	Size = height*width
	hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	
	