from libr.FreqSet1 import FreqSet
from time import sleep

"""
Run this script for IMD analysis of VTX channel group.

"""

x = FreqSet()

while True:

  x.get_input()
  converted = x.convert_freq_abbreviations()
  x.analyze_interference(converted)
  x.score(converted) 

  loop = input("\n-- Enter Q to Quit IMD Analyzer\n-- Enter X to export\n-- Press Enter to continue: \n\n").lower().strip(' ')
  if loop =='q':
    sleep(.75)
    break
  if loop == "x":
    x.export(converted)
    cont = input("-- Enter Q to Quit IMD Analyzer: ").lower().strip(' ')
    if cont =='q':
      sleep(.75)
      break
    
  print("-- Let's go again... --\n\n")
  sleep(.75)
    