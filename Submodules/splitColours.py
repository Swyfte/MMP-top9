import cv2
import numpy as np

def split(img):
	b,g,r = cv2.split(img)
	return b,g,r

def remerge(b,g,r):
	reMake = cv2.merge((b,g,r))
	return reMake

def colours(b,g,r,filename):
	redCount = cv2.countNonZero(r)
	greenCount = cv2.countNonZero(g)
	blueCount = cv2.countNonZero(b)

	# Show the images, resized smaller
	rSmall = cv2.resize(r, (480, 270))
	gSmall = cv2.resize(g, (480, 270))
	bSmall = cv2.resize(b, (480, 270))
	cv2.imshow("images", np.vstack([rSmall, gSmall, bSmall]))

	print(filename)
	print("r" + str(redCount) + " g" + str(greenCount) + " b" + str(blueCount))