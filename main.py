import cv2
import tkinter as tk
from tkinter import filedialog
from os import listdir
from os.path import isfile, join
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
	"Yellow",
	"Green",
	"Teal",
	"Cyan",
	"Blue",
	"Purple",
	"Magenta",
	"Pink",
	"Brown",
	"Grey"
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
	if symmetryCheck:
		x=1 #Call symmetry module
	if horizonCheck:
		x=1 #Call horizon module
	if vpCheck:
		x=1 #Call vanishing point module
	

def openDir():
	x=1

def makeWidgets(this):
	cb_blur = tk.Checkbutton(this, text="Blur detection", variable=blurCheck,\
		 onvalue=True, offvalue=False)
	cb_blur.grid(sticky="W",row=1,column=0)
	cb_bright = tk.Checkbutton(this, text="Brightness calculation", variable=brightCheck,\
		 onvalue=True, offvalue=False)
	cb_bright.grid(sticky="W",row=2,column=0)
	cb_colourful = tk.Checkbutton(this, text="Colourfulness", variable=colourfulCheck,\
		 onvalue=True, offvalue=False)
	cb_colourful.grid(sticky="W",row=3,column=0)
	cb_colourBal = tk.Checkbutton(this, text="Colour Balance", variable=colourBalCheck,\
		 onvalue=True, offvalue=False)
	cb_colourBal.grid(sticky="W",row=4,column=0)
	en_colourBal = tk.OptionMenu(this,showVal, *colours)
	en_colourBal.grid(sticky="W",row=4,column=1)
	cb_symmetry = tk.Checkbutton(this, text="Symmetry Detection", variable=symmetryCheck,\
		 onvalue=True, offvalue=False)
	cb_symmetry.grid(sticky="W",row=5,column=0)
	#cb_horizons = tk.Checkbutton(this, text="Horizon Detection", variable=horizonCheck,\
	#  onvalue=True, offvalue=False)
	#cb_horizons.grid(sticky="W",row=6,column=0)
	#cb_vanishing = tk.Checkbutton(this, text="Vanishing Point Detection", variable=vpCheck,\
	#  onvalue=True, offvalue=False)
	#cb_vanishing.grid(sticky="W",row=7,column=0)
	lbl_Dir = tk.Label(this, text="No album selected")
	lbl_Dir.grid(sticky="W",row=8,column=0)
	btn_Dir = tk.Button(this, text="Select album", command=openDir())
	btn_Dir.grid(sticky="W",row=8,column=1)



top = tk.Tk()
showVal = tk.StringVar()
showVal.set(colours[0])
top.title("Autophotographer")
makeWidgets(top)
#top.directory = tk.filedialog.askdirectory()
#print (top.directory)

#runModules()
top.mainloop()


"""for f in onlyfiles:
	filename = f
	img = cv2.imread(filename)"""