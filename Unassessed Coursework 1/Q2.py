# %% [markdown]
# ### Question 2: Solving Matrix-vector systems

# %% [markdown]
# 1. Solve the system of equations

# %%
import numpy as np
from sympy import symbols, Eq, solve
#define variables
x, y, z = symbols('x y z')
#define equations
eq1 = Eq(4*x - 5*y + 2*z, 7) 
eq2 = Eq(8*x + 5*y - 4*z, 10) 
eq3 = Eq(3*x - 2*y + z, 5)
#solve equations
solution = solve((eq1, eq2, eq3), (x, y, z))
print(solution) 

# %%
x,y,z = 3/2, 0, 1/2 #results taken from above output
print(4*x - 5*y + 2*z == 7)
print(8*x + 5*y - 4*z == 10)
print(3*x - 2*y + z == 5)

# %% [markdown]
# For this question, I simply import sympy and define symbols x,y and z. Then I define equations and use the solve() function to solve the equations. I print the solution. Below, I check to see if my results for x,y,z are true by subbing them back into the equations. I yield three true results which means that my values for x,y and z work for all three equations. The system of equations is thus solved.
