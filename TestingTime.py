import opiate_functions as op
import numpy as np
import matplotlib.pyplot as plt
import scipy as sc

tspan = np.arange(0, op.t_max, 1/12)
sol = op.ode_solver(tspan, op.initial_conditions, op.params)
S, P, A, R = sol[:, 0], sol[:, 1], sol[:, 2], sol[:, 3]

plt.figure()
plt.plot(tspan, P)
plt.plot(tspan, A)
plt.plot(tspan, R)
plt.show()