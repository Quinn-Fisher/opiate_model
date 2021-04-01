import opiate_functions as op
import numpy as np
import scipy as sc


def new_alpha(t_start, t_end, level, initial=0.15):

    def alpha(t):
        if t < t_start:
            al = initial
        elif t > t_start + t_end:
            al = initial
        else:
            al = level * initial
        return al

    return alpha


# def outbreak(t_start, length, level):
#     def b_p(t):
#
#         return (0.00266 * level - 0.00266) * np.e ** (- (2 / length) * (t - (t_start - length / 2)) ** 2)
#
#     def b_a(t):
#         return (0.0094 * level - 0.0094) * np.e ** (- (2 / length) * (t - (t_start - length / 2)) ** 2)
#
#     def gamma(t):
#
#         return (0.00744 * level - 0.00744) * np.e ** (- (2 / length) * (t - (t_start - length / 2)) ** 2)
#
#     return [b_p, b_a, gamma]


def outbreak(t_start, t_end, level, init_rates=(0.0026, 0.0094, 0.00744)):

    bp, ba, g = init_rates

    def b_p(t):
        if t < t_start:
            beta_p = bp
        elif t > t_end:
            beta_p = bp
        else:
            beta_p = bp * level

        return beta_p

    def b_a(t):
        if t < t_start:
            beta_a = ba
        elif t > t_end:
            beta_a = ba
        else:
            beta_a = ba * level

        return beta_a

    def gamma(t):
        if t < t_start:
            gamma_ = g
        elif t > t_end:
            gamma_ = g
        else:
            gamma_ = g * level

        return gamma_

    return [b_p, b_a, gamma]


def p_control_sim(ob_start, ob_end, ob_m, l_len, t_total, initial_conditions=(0.056, 0.0057, 0.0021, op.initN, 0.0057, 0.0056),
                  initial_rates=(0.15, 0.00266, 0.0094, 0.00744)):

    a_init, bp_init, ba_init, g_init = initial_rates

    addict_rates = [bp_init, ba_init, g_init]

    cost_array = []

    for i in np.arange(0, 1, 0.02):
        timed_alpha = [new_alpha(j, j + l_len, i, a_init) for j in np.arange(0, t_total, 0.01)]

        params_list = [
            [timed_alpha[j], op.epsilon, outbreak(ob_start, ob_end, ob_m, addict_rates)[0],
             outbreak(ob_start, ob_end, ob_m, addict_rates)[1],
             outbreak(ob_start, ob_end, ob_m, addict_rates)[2], op.zeta, op.delta, op.sigma, op.mu, op.mu_s] for j in
            range(0, len(timed_alpha))]

        cost_list = [op.con_cost(np.arange(0, t_total, op.dt), initial_conditions, params_list[j], 1, 1) for j in
                     range(0, len(params_list))]

        cost_list = np.array(cost_list)

        cost_array.append(cost_list)

    cost_array = np.array(cost_array)

    return cost_array

