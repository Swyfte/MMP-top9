import cv2
from skimage.measure import compare_ssim as ssim
import Submodules as sb

def symmTest(img,filename):
	height, width, colour = img.shape
	if width > 1000 or height > 1000:
		if width > height:
			scaleBy = 1000/width
		else:
			scaleBy = 1000/height
	else:
		scaleBy = 1
	half = int(width/2)
	dim = (int(half * scaleBy), int(height * scaleBy))
	blur = cv2.GaussianBlur(img, (7,7),0)
	grey = sb.grey(blur)

	leftSide = grey[:, :half]
	lftSml = cv2.resize(leftSide, dim)
	cv2.imshow("cropped", lftSml)
	cv2.waitKey(0)
	
	mirror = cv2.flip(leftSide, 1)
	mirSml = cv2.resize(mirror, dim)
	cv2.imshow("flipped", mirSml)
	cv2.waitKey(0)

	if width%2==0:
		rightSide = grey[:, half:]
	else:
		rightSide = grey[:, half+1:]
	rgtSml = cv2.resize(rightSide, dim)
	cv2.imshow("right", rgtSml)
	cv2.waitKey(0)

	compared = cv2.bitwise_and(mirror, rightSide)
	sim = ssim(mirror, rightSide)
	cpdSml = cv2.resize(compared, dim)
	cv2.imshow(filename + " SSIM: " + str(sim), cpdSml)
	cv2.waitKey(0)
	if sim > 0.75:
		return True
	else:
		return False

def symm(img):
	height, width, colour = img.shape
	half = int(width/2)
	blur = cv2.GaussianBlur(img, (7,7),0)
	grey = sb.grey(blur)
	leftSide = grey[:, :half]
	mirror = cv2.flip(leftSide, 1)
	if width%2==0:
		rightSide = grey[:, half:]
	else:
		rightSide = grey[:, half+1:]
	sim = ssim(mirror, rightSide)
	if sim > 0.75:
		return True
	else:
		return False