import cv2
import Submodules as sb

def brightnessTest(img, filename):
	grey = sb.greyTest(img)
	ret,thresh = sb.threshTest(grey)
	return sb.whiteCountTest(thresh,filename)
	
def brightness(img):
	grey = sb.grey(img)
	ret,thresh = sb.thresh(grey)
	return sb.whiteCount(thresh)