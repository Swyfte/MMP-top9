import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage.measure import compare_ssim as ssim

mypath = "D:\Arianwen\Documents\GitHub\MMP-top9"
filename = ""
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and (".jpg" in f))]

variance = int(input("Enter Variance: "))

## Loop through and find half of each image, flip it, then compare the two halves
# All "imshow" instances are for demonstating this module
for f in onlyfiles:
	filename = f
	img = cv2.imread(filename)
	height, width, colour = img.shape
	half = int(width/2)
	#dim = (int(half * 50/100), int(height * 50/100))

	leftSide = img[:, :half, :]
	bigdblLeft = np.zeros((height,width,colour), np.uint8)
	bigdblRght = np.zeros((height,width,colour), np.uint8)

	bigdblLeft[:, variance:half+variance, :] = leftSide
	mirror = cv2.flip(leftSide, 1)
	bigdblLeft[:, half+variance:, :] = mirror[:,variance:,:]
	dblLeft = bigdblLeft[:, variance:,:]
	#LftSml = cv2.resize(dblLeft, dim)
	#cv2.imshow("flipped", LftSml)
	#cv2.imshow("flipped", dblLeft)
	#cv2.waitKey(0)

	## Crop the left off the image to get just the right hand side
	rightSide = img[:, half:, :]
	bigdblRght[:, half+variance:, :] = rightSide[:,variance:,:]
	mirror2 = cv2.flip(rightSide, 1)
	bigdblRght[:, variance:half+variance, :] = mirror2
	dblRght = bigdblRght[:, variance:,:]
	#rgtSml = cv2.resize(dblRght, dim)
	#cv2.imshow("right", rgtSml)
	#cv2.imshow("right", dblRght)
	#cv2.waitKey(0)

	filenameL = "left_" + str(variance) + "_" + filename
	## save the image out to the new filename
	saveLoc = join(mypath, filenameL)
	cv2.imwrite(saveLoc, dblLeft)
	filenameR = "rght_"+ str(variance) + "_" + filename
	## save the image out to the new filename
	saveLoc = join(mypath, filenameR)
	cv2.imwrite(saveLoc, dblRght)