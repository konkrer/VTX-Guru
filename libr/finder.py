from libr.FreqSet1 import FreqSet
from libr.sorter import get_score
from time import sleep






def smart_lookup(num_pilots=None, usa_only=None, group_to_find=None):

	entered_f8 = False

	if not num_pilots:
		print("""
			

			
===========================================================================
$$$$$$$$$$$$$$$$$$$$$$$$$$$$>SMART SEARCH<$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
===========================================================================


			      ~ VTX Guru ~
			      Smart Search

	   VTX Channel Group Recomendation Engine


For finding a high clarity VTX channel group for 3 to 6 FPV pilots,
while ensuring as few as possible pilots need to change channels.



		
-- Enter number of pilots that will be flying at once.

""")
		while True:

			num_pilots = input("-- (Enter number in range 3 - 6) ==> ")

			if (num_pilots=='3') or (num_pilots=='4') or \
			(num_pilots=='5') or (num_pilots=='6'):
				print("\n\n---------------- Search {} Channel Groups ----------------\n".format(num_pilots))
				break
			print("\n---- Try again. ----\n")


	if not usa_only:

		while True:

			usa_only = input('\n\n-- U.S. legal channels only?\n\n-- (Enter Y or N) ==> ').lower()
			if usa_only == 'y':
				usa_only = True
				print("\n\n------------------------ USA ONLY ------------------------\n")
				if int(num_pilots) != 6:
					
					break
				else:
					print("""
  ** You selceted U.S. channels only and are looking for a 6 channel group. **
  ** THERE ARE ONLY 8 CHANNEL GROUPS IN THIS SET WITH A PASSING SCORE!      **
  ** Some U.S. VTX channels cannot be found at all in this list!            **

""")
					sleep(3)
					break


			if usa_only == 'n':
				usa_only = False
				print("\n\n----------------- 40 Channel ---------------------------\n")
				break
			print("\n---- Try again. ----")


	if not group_to_find:
		
		print("""
-- Enter VTX channels that pilots are already on. -----

   VTX Guru will find the best rated group that contains
   as many of the given channels as possible. Only groups 
   possessing a passing video clarity score are searched.

   (If some pilots can change channels eaisly and some 
   cannot, you may want to enter only the difficult to 
   change channels.)  
""")
		while True:
			group_to_find = []
			freqy = FreqSet()
			freqy.get_input(False, num_pilots, 1)

			#print(freqy.group) # -----------debug

			if ('f8' in freqy.group):
				if ('f8' in freqy.group) and ('r7' in freqy.group):
					print("** F8 and R7 are the same frequency, 5880 MHz.\n** Only enter one or the other. Two pilots cannot use the same frequency.\n\n")
					sleep(3)
					continue


				else:				
					entered_f8 = True
					

			for freq in freqy.group:
				if freq:
					if freq[0] == 'c':
						print('** All C band channels will be converted to R band. (E.g. C4 becomes R4) **\n\n')
						break

			digit_list = freqy.convert_freq_abbreviations() # to make sure C channels are converted to R.
			freqy.group = digit_list 					   # to make sure C channels are converted to R.


			group_to_find_raw = freqy.convert_to_abbreviations()
			
			#print(group_to_find_raw) # -----------debug

			for chan in group_to_find_raw:
				if chan not in group_to_find:
					group_to_find.append(chan)		
			
			#print(group_to_find) # -----------debug
			
			if usa_only:
				if ('e4' in group_to_find) or ('e7' in group_to_find)\
				or ('e8' in group_to_find):
					print("-- E4, E7, and E8 cannot be looked for in U.S. only channels.--\n\n\n---- Try again. ----")
				else:
					break
			else:
				break

	studies = ['libr/studies/list3.txt', 
	'libr/studies/list4.txt', 
	'libr/studies/list5.txt', 
	'libr/studies/list6.txt']
	if usa_only:
		studies = ['libr/studies/list3usa.txt', 
		'libr/studies/list4usa.txt', 
		'libr/studies/list5usa.txt', 
		'libr/studies/list6usa.txt']

	with open(studies[int(num_pilots) - 3]) as f:
		group_list = f.readlines()

	max_matches = 0
	max_matches_list = []

	for i in range(len(group_list)):
		matches = 0
		group = get_vtx_group(group_list[i])
		for chan in group_to_find:
			if chan in group:
				matches += 1
		if matches > max_matches:
			max_matches = matches
			max_matches_list = [i]
		elif matches == max_matches:
			max_matches_list.append(i)
	
	if max_matches == 0:
		print("""
********** No group contains any of the frequencies entered. ************


** You may just be searching U.S. legal channels for a 6 channel group 
     -or-
** Make sure to search for common VTX channels, not random frequencies.


				""")
		return

	while True:
		print("      -- Pilots on: ", end=' ')
		for chan in group_to_find:
			if entered_f8:
					if chan == 'r7':
						print('F8', end=' ')		
					else:
						print(chan.upper(), end=' ')
			else:
				print(chan.upper(), end=' ')
		print(" --")
		print('\n\n      ---- VTX Guru suggestions: ----\n')
		for i in range(len(max_matches_list)):
			idx = max_matches_list[i]
			list_line = group_list[idx]
			group = get_vtx_group(list_line)
			print('\n\n {}.'.format(i+1), end='  ')
			for chan in group:
				if entered_f8:
					if chan == 'r7':
						print('F8', end=' ')		
					else:
						print(chan.upper(), end=' ')

				else:
					print(chan.upper(), end=' ')
			if int(num_pilots) > 4:
				score = get_score(list_line, 1)
			if int(num_pilots) <=4:
				score = get_score(list_line, 0)
			print(" --   Video Clarity Score: {}".format(score))


			nextz = input('\n\n-- Press Enter to see next best group in list.\n-- Enter D if done. ===> ').lower()
			if nextz == 'd':
				
				print("\n\n")
				return
		print('\n\n----------------------- End of list, back to top of list. -----------------------\n\n')




def get_vtx_group(line):
	split1 = line.split('   ')
	split2 = split1[1].split(' -- ')
	group = split2[0].split(' ')

	return group




def get_charts():

	usa_only = False


	print("""



===========================================================================
O-O|O-O|O-O|O-O|O-O|O-O|O-O|>CHARTS EXPLORER<|O-O|O-O|O-O|O-O|O-O|O-O|O-O|O
===========================================================================

			      ~ VTX Guru ~
			     Charts Explorer





** NOTE: Channels R7 and F8 are both the same frequency - 5880 MHz.
         The charts only show 'R7' when refering to the 5880 MHz frequency.
         """)

	while True:
		num_pilots = input("""


-- Charts are organized by how many pilots will be flying at once.

-- Enter number of pilots 
-- (3 to 6) =====================> """)

		num_pilots.strip(' ')
		if (num_pilots=='3') or (num_pilots=='4') or (num_pilots=='5') or (num_pilots=='6'):
			break
		else:
			print("---- Try again ----")


	while True:
		usa_only = input("""
-- Should the chart include only 
-- U.S. legal channels?
-- (Enter Y or N) ===============> """).lower()

		if usa_only == "y":
			usa_only = True
			break
		if usa_only == 'n':
			usa_only = False
			break
		else:
			print("---- Try again ----")

	studies = [
	'libr/studies/markd_up/list3.txt', 
	'libr/studies/markd_up/list4.txt', 
	'libr/studies/markd_up/list5.txt', 
	'libr/studies/markd_up/list6.txt']

	if usa_only:
		studies = ['libr/studies/markd_up/list3usa.txt', 
		'libr/studies/markd_up/list4usa.txt', 
		'libr/studies/markd_up/list5usa.txt', 
		'libr/studies/markd_up/list6usa.txt']

	f = open(studies[int(num_pilots) - 3])
	first_line = f.readline()
	second_line = f.readline()
	third_line = f.readline()

	enumerate_num = 1
	print("\n\n\n\n")
	while True:
		
		print('\n' + "     " + first_line  + second_line + "     " + third_line)
		for i in range(50):
			x = f.readline()
			if (x == ""):
				return
			y = x.replace('100.0', '100 ')
			if enumerate_num < 10:
				print("{}.    ".format(enumerate_num) + y, end='')
			elif enumerate_num < 100:
				print("{}.   ".format(enumerate_num) + y, end='')
			elif enumerate_num < 1000:
				print("{}.  ".format(enumerate_num) + y, end='') 
			else:
				print("{}. ".format(enumerate_num) + y, end='')
			enumerate_num +=1
		more = input("\n\nPress Enter for more results. Press Q to Quit ====> ").lower()
		more.strip(' ')
		if more == 'q':
				break
		print('\n')
			
	f.close()