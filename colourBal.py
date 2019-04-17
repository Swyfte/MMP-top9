import cv2
import numpy as np
from matplotlib import pyplot as plt

mypath = "D:\Arianwen\Documents\GitHub\MMP-top9"
filename = ""
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and (".jpg" in f))]

channels = [
	([  0, 46,126], [ 13,255,255]), #Red 1
	([  7,191,191], [ 40,255,255]), #Orange
	([  7, 46,126], [ 40,190,190]), #Brown
	([ 20, 46,126], [ 68,255,255]), #Yellow
	([ 35, 46,126], [ 67,255,255]), #Green
	([ 68, 46,126], [ 80,255,255]), #Teal
	([ 81, 46,126], [ 97,255,255]), #Cyan
	([ 98, 46,126], [125,255,255]), #Blue
	([126, 46,126], [141,255,255]), #Purple
	([142, 46,126], [152,255,255]), #Magenta
	([153, 46,126], [174,255,255]), #Pink
	([  0,  0,  0], [180, 45,125]), #Grey
	([175, 46,126], [180,255,255])  #Red 2
]
counts = [
	["RED", 0],
	["ORN", 0],
	["BRN", 0],
	["YEL", 0],
	["GRN", 0],
	["TEL", 0],
	["CYN", 0],
	["BLU", 0],
	["PPL", 0],
	["MGN", 0],
	["PNK", 0],
	["GRY", 0],
]

for f in onlyfiles:
	filename = f
	img = cv2.imread(filename) 
	height, width, colour = img.shape
	Size = height*width
	hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	i=0

	for (lower, upper) in channels:
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")
		# Mask the image, filtering each of the colour channels.
		mask = cv2.inRange(hsvImg, lower, upper)
		masked = cv2.bitwise_and(hsvImg, hsvImg, mask = mask)
		greyMask = cv2.cvtColor(masked, cv2.COLOR_BGR2GRAY)

		if i < len(counts):
			counts[i][1] = cv2.countNonZero(greyMask)
			i += 1
		elif i == len(counts):
			counts[0][1] += cv2.countNonZero(greyMask)
	
	Max = ["", 0]
	for i in counts:
		if i[1] > Max[1]:
			Max = i
	print("\n" + filename)
	print(counts)
	print(Max)