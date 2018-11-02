from FreqSet1 import FreqSet
from time import sleep



print("=============================================================")
print("------------ET6-1\n")
x = FreqSet('5645', '5685', '5760', '5905', '5945')
x.get_input()
freq_list = x.convert_freq_abbreviations()
x.analyze_interference(freq_list)
x.score(freq_list)
  
print('--------------ET5\n')
x = FreqSet('5665', '5725', '5820', '5860', '5945')
x.get_input()
freq_list = x.convert_freq_abbreviations()
x.analyze_interference(freq_list)
x.score(freq_list)

print('--------------ET5A\n')
x = FreqSet('5665', '5752', '5800', '5866', '5905')
x.get_input()
freq_list = x.convert_freq_abbreviations()
x.analyze_interference(freq_list)
x.score(freq_list)

print('------------------ET5B\n')
x = FreqSet('5665', '5752', '5800', '5865', '5905')
x.get_input()
freq_list = x.convert_freq_abbreviations()
x.analyze_interference(freq_list)
x.score(freq_list)

print('----------------ET5C\n')
x = FreqSet('5665', '5760', '5800', '5865', '5905')
x.get_input()
freq_list = x.convert_freq_abbreviations()
x.analyze_interference(freq_list)
x.score(freq_list)

print('--------------IMD 5\n')
x = FreqSet('5685', '5760', '5800', '5860', '5905')
x.get_input()
freq_list = x.convert_freq_abbreviations()
x.analyze_interference(freq_list)
x.score(freq_list)

print('--------------disc1\n')
x = FreqSet('e4', 'e1', 'r3', 'f7', 'r8')
x.get_input()
freq_list = x.convert_freq_abbreviations()
x.analyze_interference(freq_list)
x.score(freq_list)