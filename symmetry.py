import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage.measure import compare_ssim as ssim
import Submodules as sb

mypath = "D:\Arianwen\Documents\GitHub\MMP-top9"
filename = ""
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and (".jpg" in f))]

## Loop through and find half of each image, flip it, then compare the two halves
# All "imshow" instances are for demonstating this module
for f in onlyfiles:
	filename = f
	img = cv2.imread(filename)
	## Find the dimensions of the input image
	height, width, colour = img.shape
	## Find the midpoint
	half = int(width/2)
	## Create a scale factor, if using reduced image size
	dim = (int(half * 25/100), int(height * 25/100))
	## Convert the image to greyscale, needed for the final comparisons
	blur = cv2.GaussianBlur(img, (5,5),0)
	grey = sb.grey(blur)

	## Crop the right off of the image to get just the left hand side
	leftSide = grey[:, :half]
	lftSml = cv2.resize(leftSide, dim)
	cv2.imshow("cropped", lftSml)
	#cv2.imshow("cropped", leftSide)
	cv2.waitKey(0)
	
	## Flip the cropped off left hand side of the image 
	mirror = cv2.flip(leftSide, 1)
	mirSml = cv2.resize(mirror, dim)
	cv2.imshow("flipped", mirSml)
	#cv2.imshow("flipped", mirror)
	cv2.waitKey(0)

	## Crop the left off the image to get just the right hand side
	if width%2==0:
		rightSide = grey[:, half:]
	else:
		rightSide = grey[:, half+1:]
	rgtSml = cv2.resize(rightSide, dim)
	cv2.imshow("right", rgtSml)
	#cv2.imshow("right", rightSide)
	cv2.waitKey(0)

	## Work out the SSIM of the image.
	# The "compared" image exists only for helping the user visualise the process of SSIM
	# and for displaying the differences between the two halves of the image.
	compared = cv2.bitwise_and(mirror, rightSide)
	sim = ssim(mirror, rightSide)
	cpdSml = cv2.resize(compared, dim)
	cv2.imshow(filename + "SSIM: " + str(sim), cpdSml)
	#cv2.imshow("SSIM: " + str(sim), compared)
	cv2.waitKey(0)