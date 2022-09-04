import numpy as np
from fractions import *
from functools import reduce



def solution(m):
    #Find the active and terminal states
    def detectstates(matrix):
        active = []
        terminal = []
        for ind, row in enumerate(matrix):
            if sum(row) == 0:
                terminal.append(ind)
            else:
                active.append(ind)
        return(active,terminal)

    
    def mtoarray(B):
        B = B.round().astype(int).A1                   # np.matrix --> np.array
        gcd = np.gcd.reduce(B)
        B = np.append(B, B.sum())                      # append the common denom
        return (B / gcd).astype(int)

    active, terminal = detectstates(m)

    
    if len(m) == 1:
        return [1,1]
    if len(active) == 1:
        return [1,1]

    if 0 in terminal:                                   #When s0 is terminal
        return [1] + [0]*len(terminal[1:]) + [1]
    m = np.matrix(m, dtype=float)[active, :]

    #common denominator
    dn = np.prod(m.sum(1))  
    PM = m / m.sum(1)
    P = m.sum(1)
    print(P)
    print(PM)
    print(dn)
    R = PM[:, terminal] 
    Q = PM[:, active]
    I = np.identity(len(Q))

    #F = (I-Q)^-1
    IQ = (I - Q)
    print(IQ)
    F = np.linalg.inv(IQ) #Inverse IQ
    #Take the first row then multiply it by the matrix subset R
    FR =  F[0] * R

    #Unsimplified fraction possibiliies
    L =  FR * dn / np.linalg.det(F)
    #Simplify
    return mtoarray(L)

#test cases
print(solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]))
print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))

    

        
