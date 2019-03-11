import cv2
import numpy as np
from matplotlib import pyplot as plt

mypath = "D:\Arianwen\Documents\GitHub\MMP-top9"
filename = ""
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and (".jpg" in f))]

channels = [
	([000,000,127],[127,127,255]),
	([000,127,000],[127,255,127]),
	([127,000,000],[255,127,127])
]

## Loop through and find each colour channel, masking it and counting
for f in onlyfiles:
	filename = f
	img = cv2.imread(filename) 
	height, width, colour = img.shape
	Size = height*width
	redCount, blueCount, greenCount = 0,0,0
	for (lower, upper) in channels:
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")
		# Mask the image, filtering each of the colour channels.
		mask = cv2.inRange(img, lower, upper)
		masked = cv2.bitwise_and(img, img, mask = mask)


		# Show the images, resized smaller
		imgSmall = cv2.resize(img, (960, 540))
		maskedSmall = cv2.resize(masked, (960, 540))
		cv2.imshow("images", np.hstack([imgSmall, maskedSmall]))
		cv2.waitKey(0)