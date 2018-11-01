from FreqSet1 import FreqSet
from time import sleep





while True:

  x = FreqSet()
  inital_list = x.get_input()
  freq_list = x.convert_freq_abbreviations(inital_list)
  x.analyze_interference(freq_list)
  x.score(freq_list)
  
  export = input("Would you like to export channel group to file?\n\n(Enter X to export, press Enter to continue):").lower()
  if export == "x":
    x.export()

  loop = input("\n\nEnter Q to quit. Press Enter to continue:").lower()
  if loop =='q':
  	break
  else:
  	print("\n\nLet's go again...\n\n")
  	sleep(.5)