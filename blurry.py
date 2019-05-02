import cv2
import Submodules as sb

## Import the jpg files
mypath = "D:\Arianwen\Documents\GitHub\MMP-top9"
filename = ""

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and (".jpg" in f))]

csvName = "blurryTest"
sb.csvWriteRow(csvName, ["Filename","Blurry?","Blurriness Val"])

for f in onlyfiles:
	filename = f
	img = cv2.imread(filename)
	dim = sb.setScaling(img)
	grey = sb.grey(img)
	isBlurry = False
	threshold = 100
	blurriness = cv2.Laplacian(grey, cv2.CV_64F).var()
	if blurriness < threshold:
		isBlurry = True

	"""# show the image
	cv2.putText(img, "{}: {:.2f}".format(isBlurry, blurriness), (10, 60),
		cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
	imgSml = cv2.resize(img, dim)
	cv2.imshow(filename, imgSml)
	cv2.waitKey(0)"""

	row = [filename, isBlurry, blurriness]
	sb.csvWriteRow(csvName, row)