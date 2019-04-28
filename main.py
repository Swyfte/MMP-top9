import cv2
import tkinter as tk
from tkinter import filedialog
from os import listdir
from os.path import isfile, join
from imutils import build_montages

filename = ""
blurCheck = symmetryCheck = colourBalCheck = colourfulCheck = brightCheck = False
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
		x=1

def onClick():
	x=1

def makecbs(this):
	cb_blur = tk.Checkbutton(this, text="Blur detection", variable=blurCheck, onvalue=True, offvalue=False)
	cb_blur.grid(sticky="W",row=1,column=0)
	cb_bright = tk.Checkbutton(this, text="Brightness calculation", variable=brightCheck, onvalue=True, offvalue=False)
	cb_bright.grid(sticky="W",row=2,column=0)
	cb_colourful = tk.Checkbutton(this, text="Colourfulness", variable=colourfulCheck, onvalue=True, offvalue=False)
	cb_colourful.grid(sticky="W",row=3,column=0)
	cb_colourBal = tk.Checkbutton(this, text="Colour Balance", variable=colourBalCheck, onvalue=True, offvalue=False)
	cb_colourBal.grid(sticky="W",row=4,column=0)
	en_colourBal = tk.OptionMenu(this,"Red", *colours)
	en_colourBal.grid(sticky="W",row=4,column=1)
	cb_symmetry = tk.Checkbutton(this, text="Symmetry Detection", variable=symmetryCheck, onvalue=True, offvalue=False)
	cb_symmetry.grid(sticky="W",row=5,column=0)


top = tk.Tk()
top.title("Autophotographer")
makecbs(top)
#top.directory = tk.filedialog.askdirectory()
#print (top.directory)
top.mainloop()


"""for f in onlyfiles:
	filename = f
	img = cv2.imread(filename)"""