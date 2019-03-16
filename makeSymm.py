import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage.measure import compare_ssim as ssim

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
	height, width, colour = img.shape
	variance = 20
	half = int(width/2)
	#dim = (int(half * 50/100), int(height * 50/100))

	leftSide = img[:, :half, :]
	dblLeft = np.zeros((height,width,colour), np.uint8)
	dblRght = np.zeros((height,width,colour), np.uint8)
	dblLeft[:, variance:half, :] = leftSide[:,:-variance,:]
	mirror = cv2.flip(leftSide, 1)
	dblLeft[:, half:-variance, :] = mirror[:,variance:,:]
	#LftSml = cv2.resize(dblLeft, dim)
	#cv2.imshow("flipped", LftSml)
	cv2.imshow("flipped", dblLeft)
	cv2.waitKey(0)

	## Crop the left off the image to get just the right hand side
	rightSide = img[:, half:, :]
	dblRght[:, half+variance:, :] = rightSide[:,variance:,:]
	mirror2 = cv2.flip(rightSide, 1)
	dblRght[:, (2*variance):half+variance, :] = mirror2[:,:-variance,:]
	#rgtSml = cv2.resize(dblRght, dim)
	#cv2.imshow("right", rgtSml)
	cv2.imshow("right", dblRght)
	cv2.waitKey(0)

	"""filename = "left_" + filename
	## save the image out to the new filename
	saveLoc = join(mypath, filename)
	cv2.imwrite(saveLoc, dblLeft)
	filename = "rght_" + filename
	## save the image out to the new filename
	saveLoc = join(mypath, filename)
	cv2.imwrite(saveLoc, dblRght)"""