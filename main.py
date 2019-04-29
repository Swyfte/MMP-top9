import cv2
import tkinter as tk
from tkinter import filedialog
from os import listdir, getcwd
from os.path import isfile, join, dirname
from imutils import build_montages
import Modules as m

filename = ""
blurCheck = horizonCheck = symmetryCheck = False
colourBalCheck = colourfulCheck = brightCheck = False
vpCheck = False
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
	onlyfiles = [f for f in listdir(fileLoc) if (isfile(join(fileLoc, f))\
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
	top.directory = tk.filedialog.askdirectory(initialdir=dirname(cwd),\
		 mustexist = True, title="Select Photo Album")

def makeWidgets(this):
	cb_blur = tk.Checkbutton(this, text="Blur detection", variable=blurCheck,\
		 onvalue=True, offvalue=False)
	cb_blur.grid(sticky="W",row=2,column=1)
	cb_bright = tk.Checkbutton(this, text="Brightness calculation", variable=brightCheck,\
		 onvalue=True, offvalue=False)
	cb_bright.grid(sticky="W",row=3,column=1)
	cb_colourful = tk.Checkbutton(this, text="Colourfulness", variable=colourfulCheck,\
		 onvalue=True, offvalue=False)
	cb_colourful.grid(sticky="W",row=4,column=1)
	cb_colourBal = tk.Checkbutton(this, text="Colour Balance", variable=colourBalCheck,\
		 onvalue=True, offvalue=False)
	cb_colourBal.grid(sticky="W",row=5,column=1)
	en_colourBal = tk.OptionMenu(this,showVal, *colours)
	en_colourBal.grid(sticky="W",row=5,column=2)
	cb_symmetry = tk.Checkbutton(this, text="Symmetry Detection", variable=symmetryCheck,\
		 onvalue=True, offvalue=False)
	cb_symmetry.grid(sticky="W",row=6,column=1)
	#cb_horizons = tk.Checkbutton(this, text="Horizon Detection", variable=horizonCheck,\
	#  onvalue=True, offvalue=False)
	#cb_horizons.grid(sticky="W",row=7,column=1)
	#cb_vanishing = tk.Checkbutton(this, text="Vanishing Point Detection", variable=vpCheck,\
	#  onvalue=True, offvalue=False)
	#cb_vanishing.grid(sticky="W",row=8,column=1)
	lbl_Dir = tk.Label(this, text="No album selected")
	lbl_Dir.grid(sticky="W",row=9,column=1)
	btn_Dir = tk.Button(this, text="Select album", command=openDir)
	btn_Dir.grid(sticky="W",row=9,column=2)



top = tk.Tk()
showVal = tk.StringVar()
showVal.set(colours[0])
top.title("Autophotographer")
makeWidgets(top)
#print (top.directory)

#runModules()
top.mainloop()


"""for f in onlyfiles:
	filename = f
	img = cv2.imread(filename)"""