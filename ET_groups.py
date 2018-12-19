from libr.FreqSet1 import FreqSet


"""
Run this script to see IMD Ace analysis of all of E.T. (http://etserv.etheli.com)
top rated  VTX channel groups.
"""


print('\n\n\n\n==========================================================')
print('=====================ET GROUPS============================')
print('==========================================================\n\n')



print('==========================================================')
print('===================ET 6 GROUPS============================')
print('==========================================================\n\n')


print("------------ETBest6\n")
x = FreqSet([5645, 5685, 5760, 5805, 5905, 5945])
freq_list = x.convert_freq_abbreviations()
x.analyze_interference(freq_list)
x.score(freq_list)
 
print('---------IMD 6C\n')
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

print("------------ET6minus1\n")
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



print('==========================================================')
print('===================ET 4 GROUP============================')
print('==========================================================\n\n')

print('--------------Raceband 4\n')
x = FreqSet([5658, 5732, 5843, 5917])
freq_list = x.convert_freq_abbreviations()
x.analyze_interference(freq_list)
x.score(freq_list)








