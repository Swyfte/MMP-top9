import cv2
import numpy as np

# This method adjusts just the contrast of an image, by multiplying by a variable alpha.
# Alpha must be between 1.0 and 3.0
def contrast(img, alpha):
	new_img = np.zeros(img.shape, img.dtype)
	new_img = cv2.convertScaleAbs(img,alpha=alpha,beta=0)
	return new_img

# This method adjusts the brightness of an image, by adding a variable beta.
# Beta must be between 0 and 100
def bright(img, beta):
	new_img = np.zeros(img.shape, img.dtype)
	new_img = cv2.convertScaleAbs(img,alpha=1.0,beta=beta)
	return new_img

# A method to allow both contrast and brightness to be adjusted at once.
# This method exists to prevent me having to call two different lines of code;
# The fewer lines of code, the less chance there is of a bug in the code.
def both(img, alpha, beta):
	new_img = np.zeros(img.shape, img.dtype)
	new_img = cv2.convertScaleAbs(img,alpha=alpha,beta=beta)
	return new_img