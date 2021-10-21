"""l=[45,"harry",789]
for i in l:
    print(i)"""

#range function: 
"""for i in range(10):      #prints from 0 to n-1 i.e till 9
    print(i)"""
"""for i in range(1,10):      #prints from 1 to n-1 i.e till 9
    print(i)
    if i==5:
        break"""
for i in range(2,10,3):       #prints from 2 to n-1 with a diff of 3
    if i==5:
        continue
    print(i)