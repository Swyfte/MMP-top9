import cv2
import tkinter as tk
from tkinter import filedialog
from os import listdir, getcwd, path
from imutils import build_montages
import Modules as m

filename = ""
blurCheck = horizonCheck = symmetryCheck = False
colourBalCheck = colourfulCheck = brightCheck = False
vpCheck = csvOut = False
onlyfiles = []
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

def runModules(img):
	if blurCheck:
		isBlurry = m.blur(img)
	if brightCheck:
		brightnessPercent = m.brightness(img)
	if colourfulCheck:
		isColourful = m.colourScale(img)
	if colourBalCheck:
		colour = showVal.get()
		mainColour = m.coloursMain(img)
		isOnColour = matchColours(colour, mainColour[0])
	if symmetryCheck:
		isSymm = m.symm(img)
#	if horizonCheck:
#		isHorizon = m.horizon(img)
#	if vpCheck:
#		isVP = m.vanpoint(img)
	
def matchColours(colour, mainColour):
	for i in colours:
		if colour == colours[i]:
			if colourCodes[i] == mainColour:
				return True
			else:
				return False

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
	x=1

def runFilterWithCSV():
	x=1

top = tk.Tk()
showVal = tk.StringVar()
showVal.set(colours[0])
top.title("Autophotographer")
cb_blur=tk.Checkbutton(top,text="Blur detection",variable=blurCheck,\
	onvalue=True,offvalue=False)
cb_blur.grid(sticky="W",row=0,column=0)
cb_bright=tk.Checkbutton(top,text="Brightness calculation",variable=brightCheck,\
	onvalue=True,offvalue=False)
cb_bright.grid(sticky="W",row=1,column=0)
cb_colourful=tk.Checkbutton(top,text="Colour Variance",variable=colourfulCheck,\
	onvalue=True,offvalue=False)
cb_colourful.grid(sticky="W",row=2,column=0)
cb_colourBal=tk.Checkbutton(top,text="Major Colour:",variable=colourBalCheck,\
	onvalue=True,offvalue=False)
cb_colourBal.grid(sticky="W",row=3,column=0)
en_colourBal=tk.OptionMenu(top,showVal,*colours)
en_colourBal.grid(sticky="W",row=3,column=1)
cb_symmetry=tk.Checkbutton(top,text="Symmetry Detection",variable=symmetryCheck,\
	onvalue=True,offvalue=False)
cb_symmetry.grid(sticky="W",row=4,column=0)
#cb_horizons=tk.Checkbutton(top,text="Horizon Detection",variable=horizonCheck,\
#	onvalue=True,offvalue=False)
#cb_horizons.grid(sticky="W",row=5,column=0)
#cb_vanishing=tk.Checkbutton(top,text="Vanishing Point Detection",variable=vpCheck,\
#	onvalue=True,offvalue=False)
#cb_vanishing.grid(sticky="W",row=6,column=0)
lbl_Dir=tk.Label(top,text="No album selected")
lbl_Dir.grid(sticky="W",row=7,column=0)
btn_Dir=tk.Button(top,text="Select album",command=openDir)
btn_Dir.grid(sticky="W",row=7,column=1)
lblPadding=tk.Label(top)
lblPadding.grid(row=0,column=2)
btn_Run=tk.Button(top,text="Run Filter",command=onClick)
btn_Run.grid(sticky="W",row=7,column=3)
cb_output=tk.Checkbutton(top,text="Create output file",variable=csvOut,\
	onvalue=True,offvalue=False)
cb_output.grid(sticky="W",row=4,column=1,columnspan=3)
#print (top.directory)

#runModules()
top.mainloop()


"""for f in onlyfiles:
	filename = f
	img = cv2.imread(filename)"""