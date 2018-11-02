from FreqSet1 import FreqSet
from time import sleep




print('==========================================================')
print('==========================================================\n\n')


print("------------ET6\n")
x = FreqSet('5645', '5685', '5760', '5805', '5905', '5945')
x.get_input()
freq_list = x.convert_freq_abbreviations()
x.analyze_interference(freq_list)
x.score(freq_list)
  
print('---------R and F band\n')
x = FreqSet('r1', 'r2', 'f2', 'f4', 'r7', 'r8')
x.get_input()
freq_list = x.convert_freq_abbreviations()
x.analyze_interference(freq_list)
x.score(freq_list)

print('---------disc1\n')
x = FreqSet('e4', 'e2', 'a4', 'f6', 'e8', 'e6')
x.get_input()
freq_list = x.convert_freq_abbreviations()
x.analyze_interference(freq_list)
x.score(freq_list)

print('---------IMD 6\n')
x = FreqSet('5645', '5685', '5760', '5800', '5860', '5905')
x.get_input()
freq_list = x.convert_freq_abbreviations()
x.analyze_interference(freq_list)
x.score(freq_list)

'''
print('ET5C\n')
x = FreqSet('5665', '5760', '5800', '5865', '5905')
inital_list = x.get_input()
freq_list = x.convert_freq_abbreviations(inital_list)
x.analyze_interference(freq_list)
x.score(freq_list)

print('IMD 5\n')
x = FreqSet('5685', '5760', '5800', '5860', '5905')
inital_list = x.get_input()
freq_list = x.convert_freq_abbreviations(inital_list)
x.analyze_interference(freq_list)
x.score(freq_list)
'''