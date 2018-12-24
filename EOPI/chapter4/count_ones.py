# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 09:56:26 2018

@author: windr
"""

"""
Check Hacker's delight 2nd edition Chapter 5 Counting bits
"""

# Good for sparsely populated words
def count_ones0(x):
    count = 0 
    while x:
        count += 1
        x &= (x-1)
        #x -= x & -x
    return count


# branch free. 
def count_ones1(x):
    y = ((x >> 1) & 0x55555555) + (x & 0x55555555) # <= 0x55555555
    y = ((y >> 2) & 0x33333333) + (y & 0x33333333) # <= 0x44444444
    y = ((y >> 4) & 0x0F0F0F0F) + (y & 0x0F0F0F0F) # <= 0x08080808
    y = (y >> 8)  + y 
    return ((y >> 16) + y) & 0xff 

# less instructions than count_ones1
def count_ones2(x):
    y = x - ((x >> 1) & 0x55555555)    # <= 0x55555555
    y = ((y >> 2) & 0x33333333) + (y & 0x33333333) # <= 0x44444444
    y = (y + (y >> 4)) & 0x0F0F0F0F   # <= 0x08080808
    y = (y >> 8)  + y 
    return ((y >> 16) + y) & 0xff 

"""
More: table based approach.
"""

X = [0xFFFFFFFF, 0x30305050, 0x12345678]

for x in X:
    print(hex(x), count_ones0(x), count_ones1(x), count_ones2(x))
    