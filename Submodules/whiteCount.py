import cv2

def whiteCount(img):
	whiteCount = 0
	Size = img.size
	whiteCount = cv2.countNonZero(img)
	value = (float(whiteCount)/Size)*100
	return value

def whiteCountTesting(img, filename):
	blackCount = 0
	whiteCount = 0
	height, width = img.shape
	Size = img.size
	print()
	print(filename)
	print("size " + str(Size))
	whiteCount = cv2.countNonZero(img)
	print("w/c " + str(whiteCount))
	blackCount = Size - whiteCount
	print("b/c " + str(blackCount))
	value = (float(whiteCount)/Size)*100
	if value > 0.5:
		print("white, " + str(round(value, 2)) + "% white")
	else:
		print("black, " + str(round(value, 2)) + "% white")
	print("height and width :", height, width)
