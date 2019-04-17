import cv2
import Submodules as sb

def blurTest(img, filename):
	height, width, colour = img.shape
	if width > 1000 or height > 1000:
		if width > height:
			scaleBy = 1000/width
		else:
			scaleBy = 1000/height
	else:
		scaleBy = 1
	dim = (int(width * scaleBy), int(height * scaleBy))
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