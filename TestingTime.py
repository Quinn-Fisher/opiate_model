import opiate_functions as op
import numpy as np
import matplotlib.pyplot as plt
import scipy as sc

tspan = np.arange(0, op.t_max, op.time_step)
sol = op.ode_solver(tspan, op.initial_conditions, op.params)
S, P, A, R, AC, RC = sol[:, 0], sol[:, 1], sol[:, 2], sol[:, 3], sol[:, 4], sol[:, 5]

plt.figure()
plt.plot(tspan, P)
plt.plot(tspan, A)
plt.plot(tspan, R)
plt.plot(tspan, AC, label='AC')
plt.plot(tspan, RC, label='RC')
plt.legend()
plt.show()
# Approximate integral of A by summing elements
sumA = sum(A) * op.time_step

print(sumA, AC[len(AC) - 1])
