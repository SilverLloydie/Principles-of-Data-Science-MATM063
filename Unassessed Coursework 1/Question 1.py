#Defining an arbitrary 4x4 Matrix A
import numpy as np
A = np.array([[1,2,3,4],[9,4,3,2],[6,6,1,9],[9,8,7,6]])
#Find the transpose, trace, determinant and inverse
A_transpose = A.T
A_trace = np.trace(A)
A_determinant = np.linalg.det(A)
A_inverse = np.linalg.inv(A)
#print results
print(A_transpose)
print(A_trace)
print(A_determinant)
print(A_inverse)
#Define cyclic matrix C
C = np.array([[0,0,1],[1,0,0],[0,1,0]])
#Calculating smallest n s.t C^n = I(3x3)
#start n from 1, as any matrix to the power of 0 becomes the identity so this is trivial
n = 1
I = np.identity(3)
while not np.array_equal(np.linalg.matrix_power(C, n), I):
    n += 1

print(f"The smallest value for n to satisfy C^n = I(3x3) is {n}")
