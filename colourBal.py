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
	redCount, blueCount, greenCount = 0,0,0
	loopNum = 0
	for (lower, upper) in channels:
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")
		# Mask the image, filtering each of the colour channels.
		mask = cv2.inRange(img, lower, upper)
		masked = cv2.bitwise_and(img, img, mask = mask)

		greyMask = cv2.cvtColor(masked, cv2.COLOR_BGR2GRAY)
		if loopNum == 0:
			redCount = cv2.countNonZero(greyMask)
			loopNum += 1
		elif loopNum == 1:
			greenCount = cv2.countNonZero(greyMask)
			loopNum += 1
		elif loopNum == 2:
			blueCount = cv2.countNonZero(greyMask)
			loopNum += 1
		else:
			loopNum = 0

		# Show the images
		cv2.imshow("image", masked)
		cv2.waitKey(0)
	
	print(str(Size))
	print("r" + str(redCount) + " g" + str(greenCount) + " b" + str(blueCount))
	if (redCount > greenCount) and (redCount > blueCount):
		print("Red Major")
	elif (greenCount > redCount) and (greenCount > blueCount):
		print("Green Major")
	elif (blueCount > redCount) and (blueCount > greenCount):
		print("Blue Major")
	else:
		print("No Major")
