from time import sleep


while True:
	
	print("""\n\n\n\n
=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
|o7o|o7o|o7o|o7o|o7o|o7o|o7o|o7o|>GURU<|o7o|o7o|o7o|o7o|o7o|o7o|o7o|o7o|o7o|
=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=


			       ~ VTX GURU ~

	 	     FPV MULTI PILOT VIDEO CLARITY TOOLS




-- 1. Smart Search - Find a low interference VTX channel group, working with
                     the channels pilots are already on.

-- 2. IMD Analyzer - Analyzes entered 5 GHZ VTX channel group
                     and produces video clarity score.

-- 3. Charts       - Look at charts of VTX groups that have a passing video
                     clarity score. See what the best scoring groups are!                  


-- 4. About VTX GURU - How the scores are calculated. 
		



		""")

	choice = input("-- Enter the number for the tool you'd like to use.\n\n-- Enter Q to quit VTX Guru. ==========> ").lower()

	if choice == '1':
		sleep(.5)
		exec(open('Smart_Search.py').read())
	elif choice == '2':
		sleep(.5)
		exec(open('IMD_Analyzer.py').read())
	elif choice == 'q':
		print('\n\n')
		break
	else:
		sleep(1)
		print("\n\n-- Not a valid choice. Let's try again. --\n\n")
		sleep(1)



	
	
	