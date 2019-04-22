import cv2
import Submodules as sb

def blurTest(img, filename):
	dim = sb.setScaling(img)
	grey = sb.grey(img)
	text = "Not blurry"
	threshold = 100
	blurriness = cv2.Laplacian(grey, cv2.CV_64F).var()
	if blurriness < threshold:
		text = "Blurry"

	# show the image
	cv2.putText(img, "{}: {:.2f}".format(text, blurriness), (10, 60),
		cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
	imgSml = cv2.resize(img, dim)
	cv2.imshow(filename, imgSml)
	cv2.waitKey(0)
	if blurriness < threshold:
		return False
	else:
		return True

def blur(img):
	grey = sb.grey(img)
	threshold = 100
	blurriness = cv2.Laplacian(grey, cv2.CV_64F).var()
	if blurriness < threshold:
		return False
	else:
		return True