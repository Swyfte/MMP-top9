import cv2
import numpy as np
from matplotlib import pyplot as plt
from os.path import join

def whiteCount(img, filename):
	blackCount = 0
	whiteCount = 0
	height, width = img.shape
	Size = img.size
	print()
	print(filename)
	print("size " + str(Size))
	whiteCount = cv2.countNonZero(img)
	print("w/c " + str(whiteCount))
	blackCount = Size - whiteCount
	print("b/c " + str(blackCount))
	if float(whiteCount)/Size > 0.5:
		print("white, " + str(round((float(whiteCount)/Size)*100, 2)) + "% white")
	else:
		print("black, " + str(round((float(whiteCount)/Size)*100, 2)) + "% white")
	print("height and width :", height, width)
