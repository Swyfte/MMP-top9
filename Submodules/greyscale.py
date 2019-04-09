import cv2
from os.path import join

def greySave(img, mypath, filename):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	filename = "gray_" + filename
	saveLoc = join(mypath, filename)
	cv2.imwrite(saveLoc, gray)

def grey(img):
	return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)