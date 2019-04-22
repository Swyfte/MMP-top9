def setScaling(img):
	height, width, colour = img.shape
	if width > 1000 or height > 1000:
		if width > height:
			scaleBy = 1000/width
		else:
			scaleBy = 1000/height
	else:
		scaleBy = 1
	return (int(width * scaleBy), int(height * scaleBy))