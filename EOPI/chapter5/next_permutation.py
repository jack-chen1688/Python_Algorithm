# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 22:04:07 2018

@author: xuehua
"""

def next_perm(perm):
    
    found = None
    for i in range(len(perm) - 1, 0, -1):
        if perm[i] > perm[i-1]:
            found = i 
            break
    if found == None:
        return perm[::-1]
    
    result = []
    print("found", found)
    for i in range(len(perm) - 1, found - 1, -1):
        if perm[i] < perm[found - 1]:
            result.append(perm[i])
        else:
            result.append(perm[found -1])
            result.extend(perm[i-1:found-1:-1])
            result = perm[:found-1] + perm[i:i+1] + result

            break
    return result

if __name__ == "__main__":
    perm = [5,2,1,3,4,0]
    
    for i in range(10):
        nxt = next_perm(perm)
        perm = nxt
        print(nxt)
        
    