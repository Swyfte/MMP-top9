import cv2
import numpy as np
from matplotlib import pyplot as plt
from os.path import join

def threshSave(img, mypath, filename):
	ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
	filename = "thresh_" + filename
	saveLoc = join(mypath, filename)
	cv2.imwrite(saveLoc, thresh)

def thresh(img):
	return cv2.threshold(img,127,255,cv2.THRESH_BINARY)