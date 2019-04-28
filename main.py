import cv2
import tkinter as tk
from tkinter import filedialog
from os import listdir
from os.path import isfile, join
from imutils import build_montages

filename = ""
blurCheck = horizonCheck = symmetryCheck = False
colourBalCheck = colourfulCheck = brightCheck = False
vpCheck = False
colourBalText = ""
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
	onlyfiles = [f for f in listdir(fileLoc) if (isfile(join(fileLoc, f)) and (".jpg" in f))]
	return onlyfiles

def runModules():
	if blurCheck:
		x=1 #Call blur module
	if brightCheck:
		x=1 #Call brightness module
	if colourfulCheck:
		x=1 #Call colourfulness module
	if colourBalCheck:
		x=1 #Call colourBalance module with the desired colour
	if symmetryCheck:
		x=1 #Call symmetry module
	if horizonCheck:
		x=1 #Call horizon module
	if vpCheck:
		x=1 #Call vanishing point module
	

def onClick():
	x=1

def makeWidgets(this):
	cb_blur = tk.Checkbutton(this, text="Blur detection", variable=blurCheck, onvalue=True, offvalue=False)
	cb_blur.grid(sticky="W",row=1,column=0)
	cb_bright = tk.Checkbutton(this, text="Brightness calculation", variable=brightCheck, onvalue=True, offvalue=False)
	cb_bright.grid(sticky="W",row=2,column=0)
	cb_colourful = tk.Checkbutton(this, text="Colourfulness", variable=colourfulCheck, onvalue=True, offvalue=False)
	cb_colourful.grid(sticky="W",row=3,column=0)
	cb_colourBal = tk.Checkbutton(this, text="Colour Balance", variable=colourBalCheck, onvalue=True, offvalue=False)
	cb_colourBal.grid(sticky="W",row=4,column=0)
	showVal = tk.StringVar()
	showVal.set(colours[0])
	en_colourBal = tk.OptionMenu(this,showVal, *colours)
	en_colourBal.grid(sticky="W",row=4,column=1)
	cb_symmetry = tk.Checkbutton(this, text="Symmetry Detection", variable=symmetryCheck, onvalue=True, offvalue=False)
	cb_symmetry.grid(sticky="W",row=5,column=0)
	#cb_horizons = tk.Checkbutton(this, text="Horizon Detection", variable=horizonCheck, onvalue=True, offvalue=False)
	#cb_horizons.grid(sticky="W",row=6,column=0)
	#cb_vanishing = tk.Checkbutton(this, text="Vanishing Point Detection", variable=vpCheck, onvalue=True, offvalue=False)
	#cb_vanishing.grid(sticky="W",row=7,column=0)


top = tk.Tk()
top.title("Autophotographer")
makeWidgets(top)
#top.directory = tk.filedialog.askdirectory()
#print (top.directory)
top.mainloop()


"""for f in onlyfiles:
	filename = f
	img = cv2.imread(filename)"""