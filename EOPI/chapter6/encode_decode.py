# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 11:19:45 2018

@author: xuehua
"""

def encode(s):
    result = []
    count = 1
    
    for i, ch in enumerate(s[:-1]):
        if ch != s[i+1]:
            result.append(str(count) + ch)
            count = 1
        else:
            count += 1
    
    result.append(str(count) + s[-1])
    return "".join(result)

def decode(s):
    result = []
    count = 0
    for ch in s:
        if ch.isdecimal():
            count = count * 10 + int(ch)
        else:
            result.append(ch * count)
            count = 0 
    return "".join(result)        
    

if __name__== "__main__":
    s=["askjsldksssskaaaakddddd", "ksdkskkskkkkkuuuyqqq"]
    for x in s:
        y = encode(x)
        z = decode(y)
        assert(x==z)
        print(x, y, z )
        
    

            