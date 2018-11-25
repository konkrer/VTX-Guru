from libr.FreqSet1 import FreqSet
from time import sleep

"""
Run this script to see IMD analysis of all of E.T. (http://etserv.etheli.com)
top rated  VTX channel groups.
"""


print('\n\n\n\n==========================================================')
print('=====================ET GROUPS============================')
print('==========================================================\n\n')



print('==========================================================')
print('===================ET 6 GROUPS============================')
print('==========================================================\n\n')


print("------------ET6\n")
x = FreqSet([5645, 5685, 5760, 5805, 5905, 5945])
freq_list = x.convert_freq_abbreviations()
x.analyze_interference(freq_list)
x.score(freq_list)
 
print('---------R and F band\n')
x = FreqSet(['r1', 'r2', 'f2', 'f4', 'r7', 'r8'])
freq_list = x.convert_freq_abbreviations()
x.analyze_interference(freq_list)
x.score(freq_list)

print('---------IMD 6\n')
x = FreqSet(['5645', '5685', '5760', '5800', '5860', '5905'])
freq_list = x.convert_freq_abbreviations()
x.analyze_interference(freq_list)
x.score(freq_list)


print('==========================================================')
print('===================ET 5 GROUPS============================')
print('==========================================================\n\n')

print("------------ET6-1\n")
x = FreqSet(['5645', '5685', '5760', '5905', '5945'])
freq_list = x.convert_freq_abbreviations()
x.analyze_interference(freq_list)
x.score(freq_list)
  
print('--------------ET5\n')
x = FreqSet(['5665', '5725', '5820', '5860', '5945'])
freq_list = x.convert_freq_abbreviations()
x.analyze_interference(freq_list)
x.score(freq_list)

print('--------------ET5A\n')
x = FreqSet(['5665', '5752', '5800', '5866', '5905'])
freq_list = x.convert_freq_abbreviations()
x.analyze_interference(freq_list)
x.score(freq_list)

print('------------------ET5B\n')
x = FreqSet(['5665', '5752', '5800', '5865', '5905'])
freq_list = x.convert_freq_abbreviations()
x.analyze_interference(freq_list)
x.score(freq_list)

print('----------------ET5C\n')
x = FreqSet(['5665', '5760', '5800', '5865', '5905'])
freq_list = x.convert_freq_abbreviations()
x.analyze_interference(freq_list)
x.score(freq_list)

print('--------------IMD 5\n')
x = FreqSet(['5685', '5760', '5800', '5860', '5905'])
freq_list = x.convert_freq_abbreviations()
x.analyze_interference(freq_list)
x.score(freq_list)
