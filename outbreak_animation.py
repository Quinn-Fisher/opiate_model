import opiate_functions as op
import timed_functions as tf
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
kappas = np.arange(1, 6, 1)
alphas = np.arange(0, 1 + 1/3, 1/3)
ob_start = 1
ob_end = 2
tspan = np.arange(0, 4, 0.0001)


params_list = [[tf.new_alpha(1 + 2/12, 2 + 2/12, alphas[j]), op.epsilon, tf.outbreak(ob_start, ob_end, 3)[0],
                tf.outbreak(ob_start, ob_end, 3)[1],
                tf.outbreak(ob_start, ob_end, 3)[2], op.zeta, op.delta, op.sigma, op.mu, op.mu_s] for j in
               range(0, len(alphas))]

param_nolock = [op.alpha, op.epsilon, tf.outbreak(ob_start, ob_end, 1)[0],
                tf.outbreak(ob_start, ob_end, 1)[1],
                tf.outbreak(ob_start, ob_end, 1)[2], op.zeta, op.delta, op.sigma, op.mu, op.mu_s]

sol1 = op.ode_solver(tspan, op.initial_conditions, params_list[0])
sol2 = op.ode_solver(tspan, op.initial_conditions, params_list[1])
sol3 = op.ode_solver(tspan, op.initial_conditions, params_list[2])
sol4 = op.ode_solver(tspan, op.initial_conditions, params_list[3])
sol = op.ode_solver(tspan, op.initial_conditions, param_nolock)
# sol5 = op.ode_solver(tspan, op.initial_conditions, params_list[4])
# sol6 = op.ode_solver(tspan, op.initial_conditions, params_list[5])


A1 = sol1[:, 4]
A2 = sol2[:, 4]
A3 = sol3[:, 4]
A4 = sol4[:, 4]
no_out = sol[:,4]
# A5 = sol5[:, 2]
# A6 = sol6[:, 2]
start = [1 + 2/12 for i in A4]
end = [2 + 2/12 for i in A4]


plt.plot(tspan, A1, label='lambda = 0')
plt.plot(tspan, A2, label='lambda = 1 / 3')
plt.plot(tspan, A3, label='lambda = 2 / 3')
plt.plot(tspan, A4, label='lambda = 1')
plt.plot(tspan, no_out, '--', label='No Outbreak')
plt.plot(start, A4, 'g--', alpha=0.2, label='Lockdown Start')
plt.plot(end, A4, 'r--', alpha=0.2, label='Lockdown End')
# plt.plot(tspan, A5, label='lambda = 0.8')
# plt.plot(tspan, A6, label='lambda = 1')
plt.xlim(1)
plt.legend()
plt.xlabel('Time (years)')
plt.ylabel('Addiction Years per person')
plt.title('5 Year Addiction Years trend kappa = 3 Outbreak with Response')
plt.show()