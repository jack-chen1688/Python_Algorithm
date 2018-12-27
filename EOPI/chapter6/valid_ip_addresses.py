# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 09:54:52 2018

@author: xuehua
"""
"""
digits "X X X X X X X X X X X X"
pos      1 2 3 4 ...
"""

import itertools

def valid_ip_addresses(s):
    
    def valid_part(x):
        #return not (len(x) > 3 or (len(x)>1 and x[0] == "0") or int(x) > 255)
        return len(x) == 1 or (x[0] != "0" and int(x) < 256)   
    
    result = []
    for x in itertools.combinations(range(1,len(s)), 3):
        lst = [s[:x[0]], s[x[0]:x[1]], s[x[1]:x[2]], s[x[2]:]]
        if all(valid_part(x) for x in lst):
            result.append(".".join(lst))
    
    return result

if __name__ == "__main__":
    lst = ["1293212323", "223546"]
    for s in lst:
        print(s)
        print(valid_ip_addresses(s))
        print("------------------")