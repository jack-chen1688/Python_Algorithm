# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 10:58:39 2018

@author: xuehua
"""

"""
 E   !   L 
H L O W R D
   L   O

1, 5, 9
0, 2, 4, 6, 8, 10
3, 7, 
"""

def snake_string0(s):
    s0 = "".join(s[i] for i in range(1, len(s), 4))
    s1 = "".join(s[i] for i in range(0, len(s), 2))
    s2 = "".join(s[i] for i in range(3, len(s), 4))
    return s0+s1+s2

def snake_string1(s):
    return s[1::4] + s[::2] + s[3::4]

if __name__ == "__main__":
    s = ["abcdefgh", "Hello World!"]
    for x in s:
        print(x, snake_string0(x), snake_string1(x))