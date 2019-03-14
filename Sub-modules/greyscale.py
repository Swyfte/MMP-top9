import cv2

## get a list of files in the directory ideally just jpgs

mypath = "E:/MMP files/"
filename = ""

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and (".jpg" in f) and ("gray_" not in f))]


## https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory

## loop through the list "for filename in listname:"
for f in onlyfiles:
	filename = f
	## modify so this reads "filename" not test.jpg
	img = cv2.imread(filename) 
	## this should still be fine
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert it to grey 
	## create a new filename which is "grey_filename"
	## (filename being the original filename) using string concatenation
	filename = "gray_" + filename
	## save the image out to the new filename
	saveLoc = join(mypath, filename)
	cv2.imwrite(saveLoc, gray)
## end of loop/program
