from libr.finder import smart_lookup
from time import sleep

while True:
	smart_lookup()
	loop = input("\n-- Enter Q to Quit Smart Search. Press Enter to continue: \n\n").lower()
	if loop =='q':
		sleep(.5)
		break
	else:
		print("-- Let's go again... --\n\n")
		sleep(.75)