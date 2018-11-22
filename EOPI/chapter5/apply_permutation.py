def apply_perm(perm, A):
    
    for i in range(len(A)):
        next = i
        while perm[next] >= 0:
            A[i], A[perm[next]] = A[perm[next]], A[i]
            temp= perm[next]
            perm[next] -= len(perm)
            next = temp
    perm[:] = [x+len(perm) for x in perm]
    return A


perm = [4, 0, 3, 2, 1]
A = ['a', 'b', 'c', 'd', 'e']
"""
A = ['a', 'b', 'c', 'd', 'e']
i = 0
    ['e', 'b', 'c', 'd', 'a'] [-1, 0, 3, 2, 1], next = perm[4]=1
    ['b', 'e', 'c', 'd', 'a'] ]-1, 0, 3, 2, -4], next = perm[1] = 0
    ['b', 'e', 'c', 'd', 'a'] [-1, -5, 3, 2, -4] next = perm[0] = -5
"""    
    
apply_perm(perm, A)
print(A, perm)

