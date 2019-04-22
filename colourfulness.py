import cv2
import numpy as np
import csvEdit
import imutils
import Submodules as sb

def colourScale(img):
	b,g,r = sb.split(img)
	redgreen = np.absolute(r-g)
	yellowblue = np.absolute(0.5*(r+g)-b)
	rbMean = np.mean(redgreen)
	ybMean = np.mean(yellowblue)
	rbStd = np.std(redgreen)
	ybStd = np.std(yellowblue)

	stdRoot = np.sqrt((rbStd**2)+(ybStd**2))
	meanRoot = np.sqrt((rbMean**2)+(ybMean**2))

	colourful = stdRoot+(0.3*meanRoot)

	if (colourful < 80) or (colourful > 120):
		return True
	else:
		return False

def colourScaleCSV(img, filename, CSVFile):
	b,g,r = sb.split(img)
	redgreen = np.absolute(r-g)
	yellowblue = np.absolute(0.5*(r+g)-b)
	rbMean = np.mean(redgreen)
	ybMean = np.mean(yellowblue)
	rbStd = np.std(redgreen)
	ybStd = np.std(yellowblue)

	stdRoot = np.sqrt((rbStd**2)+(ybStd**2))
	meanRoot = np.sqrt((rbMean**2)+(ybMean**2))

	colourful = stdRoot+(0.3*meanRoot)

	if (colourful < 80) or (colourful > 120):
		datum = (filename,colourful,True)
		csvEdit.csvWriteRow(CSVFile,datum)
		return True
	else:
		datum = (filename,colourful,False)
		csvEdit.csvWriteRow(CSVFile,datum)
		return False

def colourScaleTest(img, filename):
	dim = sb.setScaling(img)
	b,g,r = sb.split(img)
	redgreen = np.absolute(r-g)
	yellowblue = np.absolute(0.5*(r+g)-b)
	rbMean = np.mean(redgreen)
	ybMean = np.mean(yellowblue)
	rbStd = np.std(redgreen)
	ybStd = np.std(yellowblue)

	stdRoot = np.sqrt((rbStd**2)+(ybStd**2))
	meanRoot = np.sqrt((rbMean**2)+(ybMean**2))

	colourful = stdRoot+(0.3*meanRoot)

	# show the image
	cv2.putText(img, "{:.2f}".format(colourful), (10, 60),
		cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
	imgSml = cv2.resize(img, dim)
	cv2.imshow(filename, imgSml)
	cv2.waitKey(0)
	if (colourful < 80) or (colourful > 120):
		return True
	else:
		return False