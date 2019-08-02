from libr.FreqSet1 import FreqSet
from libr.sorter import sort_list2


"""
--------------------------------------------
investigate.py - Run this script to perform an investigation.
--------------------------------------------
"""

# perform investigation and sort output


x = FreqSet()
x.investigate()
try:
    sort_list2(x.output)

except IndexError:

    print('\n-- Currently cannot sort CSV file.\n')
