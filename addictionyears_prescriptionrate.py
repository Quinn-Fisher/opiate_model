import opiate_functions as op
import timed_functions as tf
import numpy as np
import matplotlib.pyplot as plt

p_vals = np.arange(0, 0.3, 0.001)
alphas = [tf.new_alpha(0, 1, 1, initial=i) for i in p_vals]
tspan = np.arange(0, 5, 0.0001)

params_list = [[alphas[j], op.epsilon, op.beta_p, op.beta_a, op.gamma, op.zeta, op.delta, op.sigma, op.mu, op.mu_s] for
               j in range(0, len(alphas))]


AC_vals = [ op.ode_solver(tspan, op.initial_conditions, params_list[j])[:, 2] for j in range(0, len(alphas))]
# RC_vals = [ op.ode_solver(tspan, op.initial_conditions, params_list[j])[:, 3] for j in range(0, len(alphas))]


# plt.plot(p_vals, AC_vals, '-')
# plt.plot(p_vals[150], AC_vals[150], 'ro')

plt.figure()
plt.plot(tspan, AC_vals[20], label='alpha= 0.02')
plt.plot(tspan, AC_vals[35], label='alpha= 0.035')
plt.plot(tspan, AC_vals[75], label='alpha= 0.075')
plt.plot(tspan, AC_vals[150], label='alpha= 0.15')
plt.plot(tspan, AC_vals[200], label='alpha= 0.2')
plt.xlabel('Time (years)')
plt.ylabel('Proportion of Population in "A" Compartment')
plt.title('Addiction rates over 5 Years')
plt.legend()
plt.show()