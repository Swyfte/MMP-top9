import time
import winsound

def MinTimer(t):
	while t:
		mins, secs = divmod(t, 60)
		timeformat = '{:02d}:{:02d}'.format(mins, secs)
		print(timeformat, end='\r')
		time.sleep(1)
		t -= 1
	duration = 1000  # milliseconds
	freq = 440  # Hz
	winsound.Beep(freq, duration)

Work = 52*60
Rest = 17*60
cancel = False
hourcounter = 0

while not cancel:
	choice = input("[W]ork, [B]reak, [C]ancel: ")
	choice = choice.lower()
	if choice == "w":
		MinTimer(Work)
		choice = ""
		hourcounter += 1
	elif choice == "b":
		MinTimer(Rest)
		choice = ""
	elif choice == "c":
		cancel = True
		print("You worked " + str(hourcounter) + " hours")