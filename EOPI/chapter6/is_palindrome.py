# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 16:15:57 2018

@author: windr
"""
def is_palindrome(s):
    length = len(s)
    start, end = 0, length - 1
    
    while start < end:
        if not s[start].isalnum(): 
            start += 1
            
        elif not s[end].isalnum():
            end -= 1
          
        elif s[start].lower() != s[end].lower():
            return False
        else:
            start += 1
            end -= 1
        
    return True


if __name__ == "__main__":
    s = "Able was I, ere I saw Elba!"
    print(s, ":", is_palindrome(s))
    s = "Ray a Ray"
    print(s, ":", is_palindrome(s))