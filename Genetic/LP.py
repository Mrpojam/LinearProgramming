# LP:
# max Z = CX [x1, x2, ..., xn]
# s.t.
# AX <= B 
# X > 0
import numpy as np

# this is a prototype so Z = c1 * x1 + c2 * x2
def input_lp ():
    c1, c2 = map(int, input().split())
    A = []
    for i in range (2):
        a = list(map(int, input().split()))
        A.append(a)
    b = list (int, input().split())
    print (c1, c2)
    print(A)
    print(b)
    return (c1, c2, A, b)
    
def Z (c1, c2, x1, x2):
    return (c1 * x1) + (c2 * x2)

def check_conditions (x1, x2, A, b):
    X = np.array([x1, x2])
    if np.matmul(A, X) <= b:
        return True
    return False

c1, c2, A, b = input_lp()