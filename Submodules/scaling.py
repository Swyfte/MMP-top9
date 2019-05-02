def setScaling(img):
	height, width, colour = img.shape
	if width > 750 or height > 750:
		if width > height:
			scaleBy = 750/width
		else:
			scaleBy = 750/height
	else:
		scaleBy = 1
	return (int(width * scaleBy), int(height * scaleBy))