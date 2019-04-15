import time
import winsound

def MinTimer(mins):
	t = mins * 60
	secs = 0
	while t:
		timeformat = '{:02d}:{:02d}'.format(mins, secs)
		print(timeformat, end='\r')
		time.sleep(1)
		t -= 1
	duration = 1000  # milliseconds
	freq = 440  # Hz
	winsound.Beep(freq, duration)

Work = 52
Rest = 17
cancel = False

while not cancel:
	choice = input("[W]ork, [B]reak, [C]ancel: ")
	choice = choice.lower()
	if choice == "w":
		MinTimer(Work)
		choice = ""
	elif choice == "b":
		MinTimer(Rest)
		choice = ""
	elif choice == "c":
		cancel = True