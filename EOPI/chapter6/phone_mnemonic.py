# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 23:40:56 2018

@author: xuehua
"""

def phone_mnemonic0(phone_number):
    MAP = ["0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
    
    lst = []
    result = []    
    def doit(i):
        for x in MAP[int(phone_number[i])]:
            lst.append(x)
            if i == len(phone_number) - 1:
                result.append("".join(lst))
            else:
                doit(i+1)
            lst.pop()
    
    doit(0)
    return result

# Minor enhancement. Predefine lst and just modify it in-place instead of keep
# append and pop.
def phone_mnemonic1(phone_number):
    MAP = ["0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
 
    lst = [0]*len(phone_number)
    result = []
    
    def doit(i):
        for x in MAP[int(phone_number[i])]:
            lst[i] = x
            if i == len(phone_number) - 1:
                result.append("".join(lst))
            else:
                doit(i+1)
    doit(0)
    return result

# iterative approach using DFS
def phone_mnemonic2(phone_number):
    MAP = ["0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
    cnt = len(phone_number)
    combination = [0] * cnt
    result = ["".join([MAP[int(phone_number[i])][combination[i]] for i in range(cnt)])]
    
    def next_combination():
        for i in reversed(range(cnt)):
            if combination[i] < len(MAP[int(phone_number[i])]) - 1:
                combination[i] += 1
                combination[i+1:] = [0] * (cnt-1-i)
                return True
        
        return False
        
    while next_combination():
       result.append("".join([MAP[int(phone_number[i])][combination[i]] for i in range(cnt)]))
   
    return result

#iterative approach using BFS
def phone_mnemonic3(phone_number):
    cnt = len(phone_number)
    MAP = ["0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
    
    lst = [[]]
    for num in phone_number:
        lst = [x+[ch] for x in lst for ch in MAP[int(num)]]
    
    lst = ["".join(x) for x in lst]
    return lst           
    
if __name__ == "__main__":
    phone_nums = ["242", "123", "981"]
    for num in phone_nums:
        print(num, "\nmethod1", phone_mnemonic0(num))
        print("method2", phone_mnemonic1(num))
        print("method3", phone_mnemonic2(num))
        print("method4", phone_mnemonic3(num))
    
