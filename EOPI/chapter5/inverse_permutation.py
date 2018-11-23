"""
http://mathworld.wolfram.com/InversePermutation.html
An inverse permutation is a permutation in which each number and the number of the place which it occupies are exchanged. For example,

p1	=	{3,8,5,10,9,4,6,1,7,2}	

p2	=	{8,10,1,6,3,7,9,2,5,4}	

are inverse permutations, since the positions of 1, 2, 3, 4, 5, 6, 7, 8, 9, and 10 in p1 are p2, and the positions of 1, 2, 3, 4, 5, 6, 7, 8, 9, and 10 in p_2 are likewise  p_1 (Muir 1960, p. 5).

The inverse permutation of a given permutation p can be computed in the Wolfram Language using InversePermutation[p].

Inverse permutations are sometimes also called conjugate or reciprocal permutations (Muir 1960, p. 4).

https://en.wikipedia.org/wiki/Permutation
The above p1 and p2 are in the form of one-line notation mentioned in wikipedia.

If we write the cycle notation of the permutation above, we have
p1 = (3, 5, 9, 7, 6, 4, 10, 2, 8, 1)
p2 = (1, 8, 2, 10, 4, 6, 7, 9, 5, 3)

Note that 
"""

def inverse_permutation(perm):
    perm_inverse = [0] * len(perm)
    
    for i in range(len(perm_inverse)):
        perm_inverse[perm[i]] = i
    
    return perm_inverse    

def inverse_permutation_inplace(perm):
    for i in range(len(perm)):
        next0, next1 = i, perm[i]
        while perm[next1] >= 0:
            temp = perm[next1] 
            perm[next1] = next0 - len(perm)
            next0, next1 = next1, temp
            print(next0, next1)
     
    perm[:] = [x+len(perm) for x in perm]    

# zero based permutation
perms = [
         [2, 7, 4, 9, 8, 3, 5, 0, 6, 1],
         [5, 3, 2, 0, 1, 4]
        ]
for i, perm in enumerate(perms):
    
    print("------------- perm: ", perm) 
    print("inverse permuration is", inverse_permutation(perm))
    inverse_permutation_inplace(perm)
    print("after inplace update", perm)
    inverse_permutation_inplace(perm)
    print("after another inplace update", perm)



        
