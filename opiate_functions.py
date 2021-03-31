import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.integrate import odeint

# Maximum time (in years) for simulation to run
t_max = 15

# Time step of one month
dt = 1 / 12


def ode_model(z, t, alpha, epsilon, beta_p, beta_a, gamma, zeta, delta, sigma, mu, mu_s):
    """Creates  Differential equations/compartments"""

    S, P, A, R, AC, RC = z
    N = S + P + A + R

    # odeint does some weird approximations with t, so we index parameters by min(int(t), t_max - 1) just to ensure
    # that they are integer values from 0 to t_max

    dSdt = -alpha(t) * S - beta_a(t) * S * A - beta_p(t) * S * P + epsilon(t) * P + delta(t) * R + mu(t) * (P + R) \
           + mu_s(t) * A

    dPdt = alpha(t) * S - (epsilon(t) + gamma(t) + mu(t)) * P

    dAdt = gamma(t) * P + sigma(t) * R + beta_a(t) * S * A + beta_p(t) * S * P - (zeta(t)+ mu_s(t)) * A

    dRdt = zeta(t) * A - (delta(t) + sigma(t) + mu(t)) * R

    dACdt = A

    dRCdt = R

    return [dSdt, dPdt, dAdt, dRdt, dACdt, dRCdt]


def ode_solver(t, initial_conditions, params):
    """ Solves system of ODE's using initial conditions, params, and  odeint from scipy"""

    initP, initA, initR, initN, initAC, initRC = initial_conditions

    alpha, epsilon, beta_p, beta_a, gamma, zeta, delta, sigma, mu, mu_s = params

    initS = initN - (initP + initA + initR)

    res = odeint(ode_model, [initS, initP, initA, initR, initAC, initRC], t,
                 args=(alpha, epsilon, beta_p, beta_a, gamma, zeta, delta, sigma, mu, mu_s))
    return res


# Parameters as functions of time must be in the form of an array with size 1 x (t_max / dt)

initN = 1  # Initial percentage of total population: keep at 1
initP = 0  # Initial percentage of population in P compartment
initA = 0  # Initial percentage of population in A compartment
initR = 0  # Initial percentage of population in R compartment
initAC = initA
initRC = initR

# Parameter values taken from https://link.springer.com/article/10.1007/s11538-019-00605-0


def alpha(t):
    return 0.15


def epsilon(t):
    return 0.8


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


# Set up default initial conditions and parameters
initial_conditions = [initP, initA, initR, initN, initAC, initRC]
params = [alpha, epsilon, beta_p, beta_a, gamma, zeta, delta, sigma, mu, mu_s]
tspan = np.arange(0, t_max, dt)
sol = ode_solver(tspan, initial_conditions, params)
S, P, A, R = sol[:, 0], sol[:, 1], sol[:, 2], sol[:, 3]