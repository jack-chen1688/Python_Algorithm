
def replace_and_delete(size, s):
    
    # first phase
    slow, count_a = 0, 0
    for fast in range(size):
        if s[fast] != 'b':
            s[slow] = s[fast]
            slow += 1
            if s[fast] == 'a':
                count_a += 1
        
    #second phase
    #slow is the number of characters that are not 'b'. 
    #slow+count_a: number of chs at last
    dest = slow + count_a - 1

    for ch in s[slow-1::-1]:
        if ch == 'a':
            s[dest-1:dest+1] = "dd"
            dest -= 2
        else:
            s[dest] = ch
            dest -= 1
    
    return s
        

if __name__ == "__main__":
    a = ['a','b','e','b',"d", "c","e"]
    print(a)
    replace_and_delete(6, a)
    print(a)