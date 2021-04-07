import opiate_functions as op
import numpy as np
import scipy as sc
import numba


def new_alpha(t_start, t_end, level, initial=0.15):
    """Create a step prescription lock-down function given parameters"""

    def alpha(t):
        # Start time of lock-down
        if t < t_start:
            al = initial

        # End time of lock-down
        elif t > t_end:
            al = initial

        # During lock-down
        else:
            al = level * initial
        return al

    return alpha


def outbreak(t_start, t_end, level, ramp_up=2 / 12, ramp_down=2 / 12, init_rates=(0.0026, 0.0094, 0.00744)):
    bp, ba, g = init_rates
    t_sr = t_start + ramp_up
    t_er = t_end - ramp_down

    """Create outbreak addiction rate functions"""

    def b_p(t):

        if t <= t_start:
            a = bp

        elif t >= t_end:
            a = bp

        elif t_start < t < t_sr:
            a = ((level - 1) * bp / ramp_up) * (t - t_start) + bp

        elif t_sr <= t <= t_er:
            a = bp * level

        elif t_er < t < t_end:
            a = ((1 - level) * bp / ramp_down) * (t - t_end + ramp_down) + level * bp

        return a

    def b_a(t):

        if t <= t_start:
            a = ba

        elif t >= t_end:
            a = ba

        elif t_start < t < t_sr:
            a = ((level - 1) * ba / ramp_up) * (t - t_start) + ba

        elif t_sr <= t <= t_er:
            a = ba * level

        elif t_er < t < t_end:
            a = ((1 - level) * ba / ramp_down) * (t - t_end + ramp_down) + level * ba

        return a

    def gamma(t):
        if t <= t_start:
            a = g

        elif t >= t_end:
            a = g

        elif t_start < t < t_sr:
            a = ((level - 1) * g / ramp_up) * (t - t_start) + g

        elif t_sr <= t <= t_er:
            a = g * level

        elif t_er < t < t_end:
            a = ((1 - level) * g / ramp_down) * (t - t_end + ramp_down) + level * g

        return a

    return [b_p, b_a, gamma]


def p_control_sim(ob_start, ob_end, ob_m, t_total, ramp_up=2 / 12, ramp_down=2 / 12,
                  initial_conditions=(0.056, 0.0057, 0.0021, op.initN, 0.0057, 0.0056, 0.01159 * 0.0057),
                  initial_rates=(0.15, 0.00266, 0.0094, 0.00744), pop=1, a_cost=1, r_cost=0):
    """Evaluate addiction outbreak and lock-down response results """

    # Unpack Initial addiction and prescription rates
    a_init, bp_init, ba_init, g_init = initial_rates
    # Re-pack just addiction rates
    addict_rates = [bp_init, ba_init, g_init]

    cost_array = []

    # Loop through magnitude of prescription lock-down
    for i in np.arange(0, 1.05, 0.05):
        # Create list of lock-down prescription functions with magnitude i
        # Loop over various initial time of lock-down
        timed_alpha = [new_alpha(j, ob_end + 2/12, i, a_init) for j in np.arange(0, ob_end + 0.05, 0.05)]

        # Create parameter list with lock-down various alpha(t) and outbreak addiction functions as parameters
        # Other parameters remain the default values
        params_list = [
            [timed_alpha[j], op.epsilon, outbreak(ob_start, ob_end, ob_m, ramp_up, ramp_down, init_rates=addict_rates)[0],
             outbreak(ob_start, ob_end, ob_m,  ramp_up, ramp_down, init_rates=addict_rates)[1],
             outbreak(ob_start, ob_end, ob_m,  ramp_up, ramp_down, init_rates=addict_rates)[2], op.zeta, op.delta,
             op.sigma, op.mu, op.mu_s] for j in range(0, len(timed_alpha))]

        # Keep track of cost/number of addicted and rehab years over course of simulation
        cost_list = [op.con_cost(np.arange(0, t_total, op.dt), initial_conditions, params_list[j], a_cost, r_cost, pop)
                     for j in range(0, len(params_list))]

        # Turn into numpy array
        cost_list = np.array(cost_list)

        # Append to list in position i
        cost_array.append(cost_list)

    # Turn into numpy array
    cost_array = np.array(cost_array)

    return cost_array


def p_control_death(ob_start, ob_end, ob_m, l_len, t_total, ramp_up=2 / 12, ramp_down=2 / 12,
                    initial_conditions=(0.056, 0.0057, 0.0021, op.initN, 0.0057, 0.0056, 0.01159 * 0.0057),
                    initial_rates=(0.15, 0.00266, 0.0094, 0.00744), pop=1, a_cost=1, r_cost=0):
    """Evaluate addiction outbreak and lock-down response results """

    # Unpack Initial addiction and prescription rates
    a_init, bp_init, ba_init, g_init = initial_rates
    # Re-pack just addiction rates
    addict_rates = [bp_init, ba_init, g_init]

    death_array = []

    # Loop through magnitude of prescription lock-down
    for i in np.arange(0, 1.05, 0.05):
        # Create list of lock-down prescription functions with magnitude i.
        # Loop over various initial time of lock-down
        timed_alpha = [new_alpha(j, j + l_len, i, a_init) for j in np.arange(0, t_total, 0.05)]

        # Create parameter list with lock-down various alpha(t) and outbreak addiction functions as parameters
        # Other parameters remain the default values
        params_list = [
            [timed_alpha[j], op.epsilon, outbreak(ob_start, ob_end, ob_m, init_rates=addict_rates)[0],
             outbreak(ob_start, ob_end, ob_m, init_rates=addict_rates)[1],
             outbreak(ob_start, ob_end, ob_m, init_rates=addict_rates)[2], op.zeta, op.delta, op.sigma, op.mu, op.mu_s]
            for j in
            range(0, len(timed_alpha))]

        # Keep track of cost/number of addicted and rehab years over course of simulation
        death_list = [op.ode_solver(np.arange(0, t_total, op.dt), initial_conditions, params_list[j])[:, 6][-1]
                      for j in range(0, len(params_list))]

        # Turn into numpy array
        death_list_list = np.array(death_list)

        # Append to list in position i
        death_array.append(death_list)

    # Turn into numpy array
    death_array = np.array(death_array)

    return death_array
