import opiate_functions as op
import numpy as np
import scipy as sc


def new_alpha(t_start, t_end, level):
    def alpha(t):
        if t < t_start:
            al = 0.15
        elif t > t_start + t_end:
            al = 0.15
        else:
            al = level * 0.15
        return al

    return alpha


def outbreak(t_start, t_end, level):
    def b_p(t):
        if t < t_start:
            beta_p = 0.00266
        elif t > t_end:
            beta_p = 0.00266
        else:
            beta_p = 0.00266 * level

        return beta_p

    def b_a(t):
        if t < t_start:
            beta_a = 0.0094
        elif t > t_end:
            beta_a = 0.0094
        else:
            beta_a = 0.0094 * level

        return beta_a

    def gamma(t):
        if t < t_start:
            gamma_ = 0.00744
        elif t > t_end:
            gamma_ = 0.00744
        else:
            gamma_ = 0.00744 * level

        return gamma_

    return [b_p, b_a, gamma]

