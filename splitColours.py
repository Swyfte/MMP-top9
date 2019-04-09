import cv2
import numpy as np
from matplotlib import pyplot as plt

mypath = "D:\Arianwen\Documents\GitHub\MMP-top9"
filename = ""
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and (".jpg" in f))]

## Loop through and find each colour channel, masking it and counting
for f in onlyfiles:
	filename = f
	img = cv2.imread(filename) 
	height, width, colour = img.shape
	Size = height*width
	redCount, blueCount, greenCount = 0,0,0

	b,g,r = cv2.split(img)

	redCount = cv2.countNonZero(r)
	greenCount = cv2.countNonZero(g)
	blueCount = cv2.countNonZero(b)

	# Show the images, resized smaller
	imgSmall = cv2.resize(img, (480, 270))
	rSmall = cv2.resize(r, (480, 270))
	gSmall = cv2.resize(g, (480, 270))
	bSmall = cv2.resize(b, (480, 270))
	cv2.imshow("images", np.vstack([rSmall, gSmall, bSmall]))

	print(filename)
	print("r" + str(redCount) + " g" + str(greenCount) + " b" + str(blueCount))

	reMake = cv2.merge((bSmall,gSmall,rSmall))
	cv2.imshow("Remade", reMake)
	cv2.waitKey(0)