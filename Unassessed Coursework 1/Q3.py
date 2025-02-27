# %% [markdown]
# ### Question 3: Solving iteration problems

# %% [markdown]
# 1. For the given iteration, how many iterations are required for convergence with tol = 10−2, 10−3, 10−4 and 10−5? Do you think that this iteration will converge as
# n →∞? (To help understand this iteration, plot the first 100 iterates of the map by plotting the points (n, xn), n = 0, . . . , 100.))

# %%
import numpy as np
import matplotlib.pyplot as plt
#I define a function that iterates
def iterate(x0, f, tol, maxit):
    x = x0
    for i in range(maxit):
        x_next = f(x)
        if abs(x_next) < tol:
            return i+1
        x = x_next
    return maxit
#I then define a function
f = lambda x: 4 * x * (1 - x)
#I print results for different tolerances
print(iterate(0.1, f, 10**-2, 100))
print(iterate(0.1, f, 10**-3, 100))
print(iterate(0.1, f, 10**-4, 10000))
print(iterate(0.1, f, 10**-5, 10000))


# %% [markdown]
# For this question, I simply defined the iterative function, which takes an initial x value, the function it wants to iterate over, a tolerance value which is the cutoff point at which we consider it to be approximately 'converged' and the max iteration value to stop the function from going forever. I then print out the results of 4 different setups.

# %%
import numpy as np
import matplotlib.pyplot as plt
#defining a graphing function for the iterable equation
def iterate_graph(x0, f, tol, maxit):
    x = x0
    fx_vals = [x]
    for i in range(maxit):
        x_next = f(x)
        fx_vals.append(x_next)
        if abs(x_next) < tol:
            break
        x = x_next
    return fx_vals

#four different tolerance scenarios
fx_vals1 = iterate_graph(0.1, f, 10**(-2), 100)
fx_vals2 = iterate_graph(0.1, f, 10**(-3), 100)
fx_vals3 = iterate_graph(0.1, f, 10**(-4), 400)
fx_vals4 = iterate_graph(0.1, f, 0, 1000)
#setting up n values to be the same size as the fx vals lists.
n1 = np.arange(len(fx_vals1))
n2 = np.arange(len(fx_vals2))
n3 = np.arange(len(fx_vals3))
n4 = np.arange(len(fx_vals4))
#setting up plotting area
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
#plotting each one in a 2 by 2 grid for neatness
axes[0, 0].plot(n1, fx_vals1, marker="o", linestyle="-", color="b")
axes[0, 0].set_title("fx_vals1")
axes[0, 0].set_xlabel("Iteration Number")
axes[0, 0].set_ylabel("Fx Value")

axes[0, 1].plot(n2, fx_vals2, marker="s", linestyle="--", color="g")
axes[0, 1].set_title("fx_vals2")
axes[0, 1].set_xlabel("Iteration Number")
axes[0, 1].set_ylabel("Fx Value")

axes[1, 0].plot(n3, fx_vals3, marker="^", linestyle="-.", color="r")
axes[1, 0].set_title("fx_vals3")
axes[1, 0].set_xlabel("Iteration Number")
axes[1, 0].set_ylabel("Fx Value")

axes[1, 1].plot(n4, fx_vals4, marker="d", linestyle=":", color="m")
axes[1, 1].set_title("fx_vals4")
axes[1, 1].set_xlabel("Iteration Number")
axes[1, 1].set_ylabel("Fx Value")


plt.tight_layout()


plt.show()

#we see results in accordance with previously calculated numbers for convergence

# %% [markdown]
# For this function I simply modify the iterative function to add in a list called fx_vals which records each function value. I can use this to then plot below using matplotlib.

# %% [markdown]
# It is clear to see that the function will not converge as n --> infinity. The function shows a sporadic jumping between 1 and 0, and has no trend towards 0 for any amount of max iterations. 
