import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.integrate import odeint

# Maximum time (in months) for simulation to run
t_max = 150


def ode_model(z, t, alpha, epsilon, beta_p, beta_a, gamma, zeta, delta, sigma, mu, mu_s):
    """Creates  Differential equations/compartments"""

    S, P, A, R = z
    N = S + P + A + R

    # odeint does some weird approximations with t, so we index parameters by min(int(t), t_max - 1) just to ensure
    # that they are integer values from 0 to t_max

    dSdt = -alpha[min(int(t), t_max - 1)] * S - beta_a[min(int(t), t_max - 1)] * S * A - beta_p[
        min(int(t), t_max - 1)] * S * P \
           + epsilon[min(int(t), t_max - 1)] * P + delta[min(int(t), t_max - 1)] * R + mu[min(int(t), t_max - 1)] * (
                   P + R) \
           + mu_s[min(int(t), t_max - 1)] * A

    dPdt = alpha[min(int(t), t_max - 1)] * S - (epsilon[min(int(t), t_max - 1)] + gamma[min(int(t), t_max - 1)] \
                                                + mu[min(int(t), t_max - 1)]) * P

    dAdt = gamma[min(int(t), t_max - 1)] * P + sigma[min(int(t), t_max - 1)] * R \
           + beta_a[min(int(t), t_max - 1)] * S * A + beta_p[min(int(t), t_max - 1)] * S * P \
           - (zeta[min(int(t), t_max - 1)] + mu_s[min(int(t), t_max - 1)]) * A

    dRdt = zeta[min(int(t), t_max - 1)] * A - (
            delta[min(int(t), t_max - 1)] + sigma[min(int(t), t_max - 1)] + mu[min(int(t), t_max - 1)]) * R

    return [dSdt, dPdt, dAdt, dRdt]


def ode_solver(t, initial_conditions, params):
    """ Solves system of ODE's using initial conditions, params, and  odeint from scipy"""

    initP, initA, initR, initN = initial_conditions

    alpha, epsilon, beta_p, beta_a, gamma, zeta, delta, sigma, mu, mu_s = params

    initS = initN - (initP + initA + initR)

    res = odeint(ode_model, [initS, initP, initA, initR], t,
                 args=(alpha, epsilon, beta_p, beta_a, gamma, zeta, delta, sigma, mu, mu_s))
    return res


def addiction_cost(population_size, initial_conditions, params, a_cost, t_start=0, t_end=t_max):
    """
    Uses population size, initial values, parameters, and addiction social cost 
    per case to determine total social cost from t_start to t_end.
    
    a_cost must be per case per month.
    """

    if t_end > t_max or t_start > t_max:
        print('t_end or t_start is too large')

    tspan = np.arange(0, t_max, 1)
    sol = ode_solver(tspan, initial_conditions, params)
    S, P, A, R = sol[:, 0], sol[:, 1], sol[:, 2], sol[:, 3]

    # Sum total monthly percentage of addictions, multiply by population to get total number of addiction cases
    tot_addicted = sum(A[t_start: t_end]) * population_size

    return a_cost * tot_addicted


def rehab_cost(population_size, initial_conditions, params, r_cost, t_start=0, t_end=t_max):
    """
    Uses population size, initial values, parameters, and addiction social cost 
    per case to determine total social cost from t_start to t_end.
    
    r_cost must be per case per month.
    """

    if t_end > t_max or t_start > t_max:
        print('t_end or t_start is too large')

    tspan = np.arange(0, t_max, 1)
    sol = ode_solver(tspan, initial_conditions, params)
    S, P, A, R = sol[:, 0], sol[:, 1], sol[:, 2], sol[:, 3]

    # Sum total monthly percentage of people in rehab, multiply by population to get total number of rehab cases
    tot_rehab = sum(R[t_start: t_end]) * population_size

    return r_cost * tot_rehab


# Parameters as functions of time must be in the form of an array with size 1 x t_max

initN = 1  # Initial percentage of total population: keep at 1
initP = 0  # Initial percentage of population in P compartment
initA = 0  # Initial percentage of population in A compartment
initR = 0  # Initial percentage of population in R compartment

# Parameter values taken from https://link.springer.com/article/10.1007/s11538-019-00605-0 however, divided by 12 to
# get averages per month

alpha = [0.015 / 12 for i in np.arange(0, t_max, 1)]  # Prescription rate per person per month

epsilon = [0.8 / 12 for i in np.arange(0, t_max, 1)]  # End prescription without addiction (rate)

beta_p = [0.00266 / 12 for i in np.arange(0, t_max, 1)]  # Illicit addiction rate based on P-class

beta_a = [0.00094 / 12 for i in np.arange(0, t_max, 1)]  # Illicit addiction rate based on A-class

gamma = [0.00744 / 12 for i in np.arange(0, t_max, 1)]  # Prescription-induced addiction rate

zeta = [0.2 / 12 for i in np.arange(0, t_max, 1)]  # Rate of A entry into rehabilitation

delta = [0.1 / 12 for i in np.arange(0, t_max, 1)]  # Successful treatment rate

sigma = [0.9 / 12 for i in np.arange(0, t_max, 1)]  # Natural relapse rate of R-class

mu = [0.00729 / 12 for i in np.arange(0, t_max, 1)]  # Natural death rate

mu_s = [0.01159 / 12 for i in np.arange(0, t_max, 1)]  # Death rate of addicts

initial_conditions = [initP, initA, initR, initN]
params = [alpha, epsilon, beta_p, beta_a, gamma, zeta, delta, sigma, mu, mu_s]
tspan = np.arange(0, t_max, 1)
