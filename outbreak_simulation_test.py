import opiate_functions as op
import timed_functions as tf
import numpy as np
import matplotlib.pyplot as plt


# initial = [0.056, 0.0057, 0.0021, op.initN, 0.0057, 0.0056]
# span = np.arange(0, 5, 0.001)
# parameters = [op.alpha, op.epsilon, tf.outbreak(0.5, 1, 2)[0], tf.outbreak(0.5, 1, 2)[1], tf.outbreak(0.5, 1, 2)[2],
#               op.zeta, op.delta, op.sigma, op.mu, op.mu_s]
# sol1 = op.ode_solver(span, initial, parameters)
# S1, P1, A1, R1, AC1, RC1 = sol1[:, 0], sol1[:, 1], sol1[:, 2], sol1[:, 3], sol1[:, 4], sol1[:, 5]
#
# sol2 = op.ode_solver(span, initial, parameters)
# S, P, A, R, AC, RC = sol2[:, 0], sol2[:, 1], sol2[:, 2], sol2[:, 3], sol2[:, 4], sol2[:, 5]


# plt.plot(span, P1)
# plt.plot(span, A1, label="A")
# plt.plot(span, R, label="R")
# plt.legend()
# plt.show()


# Trying to find how much to increase addiction to get an 18% increase in overdoses


def betap(t):
    return 0.00266 * 6


def betaa(t):
    return 0.0094 * 6


def gam(t):
    return 0.00744 * 6


initial_conditions = [op.initP, op.initA, op.initR, op.initN, op.initAC, op.initRC, op.initD]
params = [op.alpha, op.epsilon, betap, betaa, gam, op.zeta, op.delta, op.sigma, op.mu, op.mu_s]
span = np.arange(0, 1, op.dt)
sol1 = op.ode_solver(span, initial_conditions, params)
S1, P1, A1, R1, AC1, RC1, D1 = sol1[:, 0], sol1[:, 1], sol1[:, 2], sol1[:, 3], sol1[:, 4], sol1[:, 5], sol1[:, 6]
plt.plot(op.tspan, op.AC)
plt.plot(op.tspan, op.A)
plt.show()
