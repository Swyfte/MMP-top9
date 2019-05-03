This program is developed in three tiers.

The lowest tier is the submodules tier. These are the functions that can be called by any higher tier, such as the modules tier. They perform basic functions such as resizing an image proportionally to the original size.

The middle tier is the modules tier. These are the functions that are only called by the main method. They each represent a rule of photography: Blurriness, Brightness, Colour balance, Colourfulness, Contrast and Symmetry.

The final tier is the main.py program. This is the program that should be executed via the command line.

The program consists of a GUI, the check boxes do not function, as such they are all set to true in the back end.
To operate, first choose a directory via the "Select Album" button, press "Run Filter". A dialog box will come up asking for a file name. If no input is given then it defaults to "output". If cancel is pressed, the run filter action is cancelled.

The csv file will be created in the directory you selected, and will be openable by Excel. The items in the list will be sorted in descending order of quality.