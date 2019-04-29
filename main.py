import cv2
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from os import listdir, getcwd, path
from imutils import build_montages
import Modules as m
from operator import itemgetter
import Submodules as sb

filename = ""
blurCheck = horizonCheck = symmetryCheck = True
colourBalCheck = colourfulCheck = brightCheck = True
vpCheck = csvOut = contrastCheck = True
imageList = []
blank = "Not Checked"
colours = [
	"Red",
	"Orange",
	"Brown",
	"Yellow",
	"Green",
	"Teal",
	"Cyan",
	"Blue",
	"Purple",
	"Magenta",
	"Pink",
	"Grey"
]
colourCodes = [
	"RED",
	"ORN",
	"BRN",
	"YEL",
	"GRN",
	"TEL",
	"CYN",
	"BLU",
	"PPL",
	"MGN",
	"PNK",
	"GRY"
]

def readJPGs(fileLoc):
	onlyfiles = [f for f in listdir(fileLoc) if (path.isfile(path.join(fileLoc, f))\
		 and (".jpg" in f))]
	return onlyfiles

def runModules(img,filename):
	datum = [filename]
	if blurCheck:
		isFocussed = m.blur(img)
		datum.append(isFocussed)
	else:
		datum.append(blank)
	if brightCheck:
		brightnessPercent = (m.brightness(img))*100
		datum.append(brightnessPercent)
	else:
		datum.append(blank)
	if contrastCheck:
		contrast = m.getContrastVal(img)
		goodContrast = m.getContrast(img)
		datum.append(contrast)
		datum.append(goodContrast)
	else:
		datum.append(blank)
	if colourfulCheck:
		isColourful = m.colourScale(img)
		datum.append(isColourful)
	else:
		datum.append(blank)
	if colourBalCheck:
		colour = showVal.get()
		mainColour = m.coloursMain(img)
		isOnColour = matchColours(colour, mainColour[0])
		datum.append(mainColour[0])
		datum.append(isOnColour)
	else:
		datum.append(blank)
	if symmetryCheck:
		isSymm = m.symm(img)
		datum.append(isSymm)
	else:
		datum.append(blank)
#	if horizonCheck:
#		isHorizon = m.horizon(img)
#	else:
#		datum.append(blank)
#	if vpCheck:
#		isVP = m.vanpoint(img)
#	else:
#		datum.append(blank)
	return datum
	
def matchColours(colour, mainColour):
	i = 0
	while i < len(colours):
		if colour == colours[i]:
			if colourCodes[i] == mainColour:
				return True
			else:
				return False
		i += 1

def openDir():
	cwd = getcwd()
	top.directory = tk.filedialog.askdirectory(initialdir=path.dirname(cwd),\
		mustexist = True,title="Select Photo Album")
	AlbumName = path.basename(top.directory)
	lbl_Dir.config(text=AlbumName)

def onClick():
	if csvOut:
		runFilterWithCSV()
	else:
		runFilter()

def runFilter():
	onlyfiles = readJPGs(top.directory)
	for f in onlyfiles:
		filename = f
		img = cv2.imread(filename)
		imageList.append(runModules(img,filename))
	sortedimgs = sortImgs(imageList)
	top10Data = sortedimgs[0:10]
	top10Names = []
	for i in top10Data:
		top10Names.append(i[0])
	top10Imgs = []
	for f in top10Names:
		filename = f
		img = cv2.imread(filename)
		top10Imgs.append(runModules(img,filename))
		
	build_montages(top10Imgs,[400,300],[4,3])
	cv2.montages

def runFilterWithCSV():
	response = tk.simpledialog.askstring("Enter a name for the output file:", "Defaults to output if left blank.",
                                parent=top)
	if response is not "" and response is not None:
		csvName = response
	elif response is not None:
		csvName = "output"
	else:
		messagebox.showinfo("", "Cancel pressed, action aborted")
		return
	headers = ["Filename",
			"Focused?",
			"Brightness",
			"Contrast",
			"Good Contrast?",
			"High Colour Variance?",
			"Major Colour",
			"Match Chosen Colour?",
			"Symmetrical?"]
	sb.csvWriteRow(csvName, headers)
	onlyfiles = readJPGs(top.directory)
	for f in onlyfiles:
		filename = f
		img = cv2.imread(filename)
		imageList.append(runModules(img,filename))
	sortedimgs = sortImgs(imageList)
	for i in sortedimgs:
		sb.csvWriteRow(csvName,i)
	

def sortImgs(listimgs):
	score = 0 #Used as a sorting metric. Each aspect adds a weight
	sortingList = []
	for i in listimgs:
		if i[1] is not blank:
			if i[1]: #If in focus, add 1 to score, else remove 10
				score += 1
			else:
				score -= 10
		
		if i[2] is not blank:
			if i[2] > 50.0: #If brightness > 50%...
				if i[2] > 80.0: #...and not above 80, +1. Else -4
					score -= 4
				else:
					score += 1
			elif i[2] < 20.0: #If brightness is < 20%, -4. Else -1
				score -= 4
			else:
				score -= 1

		if i[4] is not blank: #If good contrast, +2. Else -1
			if i[4]:
				score += 2
			else:
				score -= 1

		if i[5] is not blank: #If good colour, +1. Else -2
			if i[5]:
				score += 1
			else:
				score -= 2

		if i[7] is not blank: #If matches desired colour, +1. Else -10
			if i[7]:
				score += 1
			else:
				score -= 10
		
		if i[8] is not blank: #If symmetrical, +1. Else -2
			if i[8]:
				score += 1
			else:
				score -= 2
		sortingList.append([score,i]) #Create list with score
	sorted(sortingList, key=itemgetter(0)) #Sort by score
	trimScoreList = []
	finalList = []
	for i in sortingList:
		trimScoreList.append(i[1:])
	for i in trimScoreList:#Remove layer of single item lists added by previous command
		for x in i:
			finalList.append(x)
	return finalList #Return everything but score
	

top = tk.Tk()
showVal = tk.StringVar()
showVal.set(colours[0])
top.title("Autophotographer")
cb_blur=tk.Checkbutton(top,text="Blur detection",variable=blurCheck,\
	onvalue=True,offvalue=False)
cb_blur.grid(sticky="W",row=0,column=0)
cb_bright=tk.Checkbutton(top,text="Brightness calculation",variable=brightCheck,\
	onvalue=True,offvalue=False)
cb_bright.grid(sticky="W",row=2,column=0)
cb_contrast=tk.Checkbutton(top,text="Contrast calculation",variable=contrastCheck,\
	onvalue=True,offvalue=False)
cb_contrast.grid(sticky="W",row=4,column=0)
cb_colourful=tk.Checkbutton(top,text="Colour Variance",variable=colourfulCheck,\
	onvalue=True,offvalue=False)
cb_colourful.grid(sticky="W",row=3,column=0)
cb_colourBal=tk.Checkbutton(top,text="Major Colour:",variable=colourBalCheck,\
	onvalue=True,offvalue=False)
cb_colourBal.grid(sticky="W",row=4,column=0)
en_colourBal=tk.OptionMenu(top,showVal,*colours)
en_colourBal.grid(sticky="W",row=4,column=1)
cb_symmetry=tk.Checkbutton(top,text="Symmetry Detection",variable=symmetryCheck,\
	onvalue=True,offvalue=False)
cb_symmetry.grid(sticky="W",row=5,column=0)
#cb_horizons=tk.Checkbutton(top,text="Horizon Detection",variable=horizonCheck,\
#	onvalue=True,offvalue=False)
#cb_horizons.grid(sticky="W",row=65,column=0)
#cb_vanishing=tk.Checkbutton(top,text="Vanishing Point Detection",variable=vpCheck,\
#	onvalue=True,offvalue=False)
#cb_vanishing.grid(sticky="W",row=7,column=0)
lbl_Dir=tk.Label(top,text="No album selected")
lbl_Dir.grid(sticky="W",row=8,column=0)
btn_Dir=tk.Button(top,text="Select album",command=openDir)
btn_Dir.grid(sticky="W",row=8,column=1)
lblPadding=tk.Label(top)
lblPadding.grid(row=0,column=2)
btn_Run=tk.Button(top,text="Run Filter",command=onClick)
btn_Run.grid(sticky="W",row=8,column=3)
cb_output=tk.Checkbutton(top,text="Create output file",variable=csvOut,\
	onvalue=True,offvalue=False)
cb_output.grid(sticky="W",row=5,column=1,columnspan=3)
top.mainloop()