import cv2
import Submodules as sb

def blurTest(img, filename):
	dim = sb.setScaling(img)
	grey = sb.grey(img)
	isBlurry = False
	threshold = 100
	blurriness = cv2.Laplacian(grey, cv2.CV_64F).var()
	if blurriness < threshold:
		isBlurry = True

	# show the image
	cv2.putText(img, "{}: {:.2f}".format(isBlurry, blurriness), (10, 60),
		cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
	imgSml = cv2.resize(img, dim)
	cv2.imshow(filename, imgSml)
	cv2.waitKey(0)
	if blurriness < threshold:
		return False
	else:
		return True

def blurCSV(img, filename, csvName):
	grey = sb.grey(img)
	isBlurry = False
	threshold = 100
	blurriness = cv2.Laplacian(grey, cv2.CV_64F).var()
	if blurriness < threshold:
		isBlurry = True
		datum = (filename,blurriness,isBlurry)
		sb.csvWriteRow(csvName,datum)
		return False
	else:
		datum = (filename,blurriness,isBlurry)
		sb.csvWriteRow(csvName,datum)
		return True

def blur(img):
	grey = sb.grey(img)
	threshold = 100
	blurriness = cv2.Laplacian(grey, cv2.CV_64F).var()
	if blurriness < threshold:
		return False
	else:
		return True