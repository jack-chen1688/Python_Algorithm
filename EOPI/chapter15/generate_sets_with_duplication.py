# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 21:35:57 2019

@author: windr
"""

def generate_sets_with_duplication(A):
    
    A.sort()
    result = [[]]
    start = 0
    for i in range(len(A)):
        length = len(result)
        for s in result[start:]:
            result.append(s + [A[i]])
        
        if i < len(A) - 1 and A[i] == A[i+1]:
            start = length
        else:
            start = 0

    return result

def main():
    A = [1,2,3,2]    
    print (A, generate_sets_with_duplication(A)) 
    

if __name__ == "__main__":
    main()