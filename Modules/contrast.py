import cv2
import Submodules as sb
import scipy.stats as stats

def getContrastCSV(img, filename):
	csvName = "contrastTest"
	if sb.csvReadRow(csvName,0) == None:
		datum = ("filename", "Contrast","Brightness","Accepted")
		sb.csvWriteRow(csvName,datum)
	space_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

	hist_img = cv2.calcHist([space_img[0]],[0],None,[256],[0,256])
	contrast = stats.variation(hist_img,None)

	grey = sb.grey(img)
	ret, thresh = sb.thresh(grey)
	wcount = sb.whiteCount(thresh)

	accepted = True

	if (contrast-(10*wcount) < 0.1) or (wcount < 0.1):
		accepted = False
	
	datum = (filename, contrast, (wcount*100), accepted)
	sb.csvWriteRow(csvName,datum)
	return accepted

def getContrast(img):
	space_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

	hist_img = cv2.calcHist([space_img[0]],[0],None,[256],[0,256])
	contrast = stats.variation(hist_img,None)

	grey = sb.grey(img)
	ret, thresh = sb.thresh(grey)
	wcount = sb.whiteCount(thresh)
	accepted = True
	if (contrast-(10*wcount) < 0.1) or (wcount < 0.1):
		accepted = False
	return accepted