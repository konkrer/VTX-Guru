from time import sleep


while True:
	
	print("""\n\n\n\n
=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
|o7o|o7o|o7o|o7o|o7o|o7o|o7o|o7o|o7o|o7o|>GURU<|o7o|o7o|o7o|o7o|o7o|o7o|o7o|o7o|o7o|o7o|o7o|o7o
=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=


			              ~ VTX GURU ~

	 	            FPV MULTI PILOT VIDEO CLARITY TOOLS




-- 1. Smart Search   - Find a high clarity VTX channel group for 3 to 6 pilots. 
                       Works with the channels pilots are already on,
                       so as few as possible pilots need to change channel.


-- 2. IMD Ace        - Analyzes entered 5 GHZ VTX channel group
                       and produces video clarity score.

 
-- 3. Charts         - See charts of channel groups  possessing a passing video
      Explorer         clarity score. See what the best scoring groups are!


-- 4. EZ Investigate - Used to investigate all possible combinations of
                       VTX channel groups. Produces a scored list, from 
                       best to worst. (Use this if 40 channel or U.S. legal 
                       channels only doesn't meet your channel needs.)
                                                           


-- 5. What is IMD?   - IMD and why it matters for FPV pilots.


-- 6. About VTX GURU - How the scores are calculated. 
		



		""")

	while True:
		choice = input("-- Enter the number for the tool you'd like to use.\n\n-- Enter Q to Quit VTX Guru. ==========> ").lower().strip(' ')
		
		if (choice=='1') or (choice=='2') or (choice=='3') or (choice=='4') or (choice=='5') or (choice=='6') or (choice=='q'):
			break
		else:
			sleep(.5)
			print("\n\n-- Not a valid choice. Let's try again. --\n\n")
			sleep(2)

	if choice == '1':
		sleep(.5)
		exec(open('Smart_Search.py').read())
	if choice == '2':
		sleep(.5)
		exec(open('IMD_Analyzer.py').read())
	if choice == '3':
		sleep(.5)
		exec(open('Charts.py').read())
	if choice == '4':
		sleep(.5)
		exec(open('Investigate.py').read())
	if choice == '5':
		exec(open('libr/Info2.py').read())
	if choice == '6':
		exec(open('libr/Info.py').read())
	if choice == 'q':
		print('\n\n')
		break
	



	
	
	