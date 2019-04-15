import Submodules as sb
import cv2

def calcTest(img, filename):
	grey = sb.grey(img)
	ret, thresh = sb.thresh(grey)
	sb.whiteCountTesting(thresh, filename)

def calc(img):
	grey = sb.grey(img)
	ret,thresh = sb.thresh(grey)
	whiteValue = sb.whiteCount(thresh)
	return whiteValue