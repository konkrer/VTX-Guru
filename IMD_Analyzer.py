from FreqSet1 import FreqSet
from time import sleep





while True:

  x = FreqSet()
  x.get_input()
  converted = x.convert_freq_abbreviations()
  x.analyze_interference(converted)
  x.score(converted)
  
  export = input("Would you like to export channel group to file?\n\n(Enter X to export, press Enter to continue):").lower()
  if export == "x":
    x.export()

  loop = input("\n\nEnter Q to quit. Press Enter to continue:").lower()
  if loop =='q':
  	break
  else:
  	print("\n\nLet's go again...\n\n")
  	sleep(.5)