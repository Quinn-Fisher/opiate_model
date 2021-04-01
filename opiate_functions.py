import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.integrate import odeint

# Maximum time (in years) for simulation to run
t_max = 10

# Time step
dt = 0.0001


def ode_model(z, t, alpha, epsilon, beta_p, beta_a, gamma, zeta, delta, sigma, mu, mu_s):
    """Creates  Differential equations/compartments"""

    S, P, A, R, AC, RC, D = z
    N = S + P + A + R

    # Use continuous parameter functions

    dSdt = -alpha(t) * S - beta_a(t) * S * A - beta_p(t) * S * P + epsilon(t) * P + delta(t) * R + mu(t) * (P + R) \
           + mu_s(t) * A

    dPdt = alpha(t) * S - (epsilon(t) + gamma(t) + mu(t)) * P

    dAdt = gamma(t) * P + sigma(t) * R + beta_a(t) * S * A + beta_p(t) * S * P - (zeta(t) + mu_s(t)) * A

    dRdt = zeta(t) * A - (delta(t) + sigma(t) + mu(t)) * R

    # Set diff. eq. for cost functions of addiction and rehab
    dACdt = A
    dRCdt = R

    # Set diff eq. for keeping track of death

    dDdt = mu_s(t)*A
    return [dSdt, dPdt, dAdt, dRdt, dACdt, dRCdt, dDdt]


def ode_solver(t, initial_conditions, params):
    """ Solves system of ODE's using initial conditions, params, and  odeint from scipy"""

    initP, initA, initR, initN, initAC, initRC, initD = initial_conditions

    alpha, epsilon, beta_p, beta_a, gamma, zeta, delta, sigma, mu, mu_s = params

    initS = initN - (initP + initA + initR)

    res = odeint(ode_model, [initS, initP, initA, initR, initAC, initRC, initD], t,
                 args=(alpha, epsilon, beta_p, beta_a, gamma, zeta, delta, sigma, mu, mu_s))
    return res


def con_cost(t, initial_conditions, params, a_cost, r_cost, population=1):
    sol = ode_solver(t, initial_conditions, params)
    S, P, A, R, AC, RC = sol[:, 0], sol[:, 1], sol[:, 2], sol[:, 3], sol[:, 4], sol[:, 5]

    AddictCost = a_cost * population * AC[-1]
    RehabCost = r_cost * population * RC[-1]

    return AddictCost + RehabCost


# Set up some default initial conditions (WILL BE CHANGED LATER)
initN = 1  # Initial percentage of total population: keep at 1
initP = 0.056  # Initial percentage of population in P compartment
initA = 0.0057 # Initial percentage of population in A compartment
initR = 0.0021  # Initial percentage of population in R compartment
initAC = initA
initRC = initR
initD = initA * 0.01159


# Parameter values taken from https://link.springer.com/article/10.1007/s11538-019-00605-0
# Creat continuous functions for parameters

def alpha(t):
    return 0.15


def epsilon(t):
    return 2.25


def beta_p(t):
    return 0.00266


def beta_a(t):
    return 0.0094


def gamma(t):
    return 0.00744


def zeta(t):
    return 0.2


def delta(t):
    return 0.1


def sigma(t):
    return 0.9


def mu(t):
    return 0.00729


def mu_s(t):
    return 0.01159


# Set up default initial conditions, parameters, and solutions
initial_conditions = [initP, initA, initR, initN, initAC, initRC, initD]
params = [alpha, epsilon, beta_p, beta_a, gamma, zeta, delta, sigma, mu, mu_s]
tspan = np.arange(0, 1, dt)
sol = ode_solver(tspan, initial_conditions, params)
S, P, A, R, AC, RC = sol[:, 0], sol[:, 1], sol[:, 2], sol[:, 3], sol[:, 4], sol[:, 5]

D = sol[:, 6]
