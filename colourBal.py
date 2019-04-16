import cv2
import numpy as np
from matplotlib import pyplot as plt

mypath = "D:\Arianwen\Documents\GitHub\MMP-top9"
filename = ""
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and (".jpg" in f))]

Colours = [
	([  0,  0,  0], [ 13,100,100]), #Red 1
	([  7, 75, 75], [ 40,100,100]), #Orange
	([  7,  0,  0], [ 40, 74, 74]), #Brown
	([ 20,  0,  0], [ 68,100,100]), #Yellow
	([ 35,  0,  0], [134,100,100]), #Green
	([135,  0,  0], [160,100,100]), #Teal
	([161,  0,  0], [195,100,100]), #Cyan
	([196,  0,  0], [250,100,100]), #Blue
	([251,  0,  0], [282,100,100]), #Purple
	([283,  0,  0], [304,100,100]), #Magenta
	([305,  0,  0], [349,100,100]), #Pink
	([350,  0,  0], [360,100,100]), #Red 2
]

for f in onlyfiles:
	filename = f
	img = cv2.imread(filename) 
	height, width, colour = img.shape
	Size = height*width
	hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	