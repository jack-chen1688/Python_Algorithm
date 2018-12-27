# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 20:40:05 2018

@author: xuehua
"""

#number, start, end, intermediate

def hanoi_move_0(n):
    def hannoi(n, start, end, intermediate):
        if n == 0:
            return
        hannoi(n-1, start, intermediate, end)
        print("move", n, "from", start, "to", end)
        hannoi(n-1, intermediate, end, start)
   
    hannoi(n, 0, 1, 2)

def hanoi_move_1(n):
    lst = [(1, 0, 1)]
    
    for i in range(2, n+1):
        lst_next = []
        for tup in lst:
            lst_next.append((tup[0], (3-tup[1])%3, (3-tup[2])%3))
        lst_next.append((i, 0, 1))
        for tup in lst:
            lst_next.append((tup[0], (2-tup[1]) % 3, (2-tup[2])%3)) 
        
        lst = lst_next
        
    for x,y,z in lst:
        print("move", x, "from", y, "to", z)
                
for i in range(1,5):
    print("solution for hannoi", i, ":")
    print("---------------------------")
    hanoi_move_0(i)
    print("---------------------------")
    hanoi_move_1(i)
