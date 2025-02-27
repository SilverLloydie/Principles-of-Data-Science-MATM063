# %% [markdown]
# ### Question 1: Defining Matricies and Performing Operations

# %% [markdown]
# 1. Define a four by four matrix A, find its transpose, trace, determinant and inverse.

# %%
import numpy as np
#Defining an arbitrary 4x4 Matrix A
A = np.array([[1,2,3,4],[9,4,3,2],[6,6,1,9],[9,8,7,6]])
#Find the transpose, trace, determinant and inverse
A_transpose = A.T
A_trace = np.trace(A)
A_determinant = np.linalg.det(A)
A_inverse = np.linalg.inv(A)
#print results
print(f"The transpose of matrix A is:\n{A_transpose}")
print(f'The trace of matrix A is:',A_trace)
print(f'The determinant of matrix A is:',A_determinant)
print(f"The inverse of matrix A is:\n{A_inverse}")

# %% [markdown]
# For this question, I used numpy to create matrix A, then used the linalg function to calculate the matrix's properties. Finally I printed the properties.

# %% [markdown]
# 2. For the cyclic matrix C, find the smallest value of n such that C**n = I (Identity Matrix 3*3)

# %%
#Define cyclic matrix C
C = np.array([[0,0,1],[1,0,0],[0,1,0]])
#Calculating smallest n s.t C^n = I(3x3)
#start n from 1, as any matrix to the power of 0 becomes the identity so this is trivial
n = 1
I = np.identity(3)
while not np.array_equal(np.linalg.matrix_power(C, n), I):
    n += 1

print(f"The smallest value for n to satisfy C^n = I(3x3) is n = {n}")


# %% [markdown]
# For this question I create a while loop that iterates over values of n starting from 1 until the desired equation is satisfied. It then prints the according n that satisfies the equation.
