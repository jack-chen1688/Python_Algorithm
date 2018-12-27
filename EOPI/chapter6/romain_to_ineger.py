# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 23:36:30 2018

@author: xuehua
"""

import functools

def roman_to_integer0(s):
    
    MAP = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    
    result = 0
    for i in range(0, len(s) - 1):
        if MAP[s[i]] >= MAP[s[i+1]]:
            result += MAP[s[i]]
        else:
            result -= MAP[s[i]]
    
    return result + MAP[s[-1]]

if __name__ == "__main__":
    lst = ["XI", "IX", "CDX"]
    for s in lst:
        print(s, roman_to_integer0(s))
