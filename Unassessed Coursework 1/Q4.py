# %% [markdown]
# ### Question 4: Solving equations

# %% [markdown]
# 1. For the function f(x) = sin**(x) - sin(2x) - 1, show that it changes sign between x = -1 and x = 0. Find a solution of the equation f(x) = 0 between x=-1 and x = 0.

# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
# define f(x)
sin_func = lambda x: np.sin(x)**2 - np.sin(2*x) - 1
x_vals = np.linspace(-1, 0, 100)  # 100 points for smooth curve
y_vals = [sin_func(x) for x in x_vals]  # Compute y values

# Plot the function
plt.plot(x_vals, y_vals, label=r"$sin^2(x) - sin(2x) - 1$", color='b')

# Formatting
plt.axhline(0, color='black', linestyle='--', linewidth=1)  # Add x-axis
plt.axvline(0, color='black', linestyle='--', linewidth=1)  # Add y-axis
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Plot of $sin^2(x) - sin(2x) - 1$")
plt.legend()
plt.grid()

# fsolve is used to find the value of x that makes f(x) equal to zero.
solution = fsolve(sin_func, -0.1)
plt.scatter(solution, 0, color='red', zorder=3, label="Root")
print(f'The intersection of the function with the X-axis is at', solution)

# %% [markdown]
# For this question I simply define the sin function, create x values and y values in a Numpy array and plot. Then I use the fsolve() function to find the solution for f(x) = 0. I do some matplotlib formatting to make it look for visibly obvious.
