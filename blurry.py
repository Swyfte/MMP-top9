import cv2
import numpy as np
from matplotlib import pyplot as plt
import Submodules as sb


## Import the jpg files
mypath = "D:\Arianwen\Documents\GitHub\MMP-top9"
filename = ""

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and (".jpg" in f))]

for f in onlyfiles:
    filename = f
    img = cv2.imread(filename)