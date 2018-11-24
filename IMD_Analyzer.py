from libr.FreqSet1 import FreqSet
from time import sleep

"""
Run this script for IMD analysis of VTX channel group.

"""



while True:

  x = FreqSet()
  x.get_input()
  converted = x.convert_freq_abbreviations()
  x.analyze_interference(converted)
  x.score(converted)
  
  export = input("-- Would you like to export channel group to file? --\n\n-- (Enter X to export, Press Enter to continue): ").lower()
  if export == "x":
    x.export(converted)

  loop = input("\n-- Enter Q to Quit IMD Analyzer. Press Enter to continue: \n\n").lower()
  if loop =='q':
    sleep(.75)
    break
  else:
    print("-- Let's go again... --\n\n")
    sleep(.75)
    