import opiate_functions as op
import numpy as np
import timed_functions as tf
import matplotlib.pyplot as plt

ob_start = 0
ob_end = np.arange(0.5, 4.5, 0.5)
ob_m = [3, 3.5, 4, 4.5]


diff1 = []
diff2 = []
diff3 = []
diff4 = []


for j in ob_end:

    cost_array1 = np.array(tf.p_control_sim(0, j, ob_m[0], j + 5))
    cost_array2 = np.array(tf.p_control_sim(0, j, ob_m[1], j + 5))
    cost_array3 = np.array(tf.p_control_sim(0, j, ob_m[2], j + 5))
    cost_array4 = np.array(tf.p_control_sim(0, j, ob_m[3], j + 5))

    diff1.append(1 - np.amin(cost_array1) / np.amax(cost_array1))
    diff2.append(1 - np.amin(cost_array2) / np.amax(cost_array2))
    diff3.append(1 - np.amin(cost_array3) / np.amax(cost_array3))
    diff4.append(1 - np.amin(cost_array4) / np.amax(cost_array4))


plt.plot(ob_end, diff1, '--ro', label='kappa = 3')
plt.plot(ob_end, diff2, '--bo', label='kappa = 3.5')
plt.plot(ob_end, diff3, '--go', label='kappa = 4')
plt.plot(ob_end, diff4, '--co', label='kappa = 4.5')
plt.legend()
plt.xlabel('Length of Outbreak (years)')
plt.ylabel('Optimal Percentage decrease of Addiction Years')
plt.title('Optimal decrease in Addiction Years, 5 years post Outbreak')
plt.show()

print(diff1, 'hello', diff2, 'hello', diff3, 'hello', diff4)






# t = np.arange(0, 100, 0.0001)
#
# initial_conditions = op.initial_conditions
# params = [op.alpha, op.epsilon, op.beta_p, op.beta_a, op.gamma, op.zeta, op.delta, op.sigma,
#           op.mu, op.mu_s]
# sol = op.ode_solver(t, initial_conditions, params)
# S, P, A, R, AC, RC = sol[:, 0], sol[:, 1], sol[:, 2], sol[:, 3], sol[:, 4], sol[:, 5]
#
# D = sol[:, 6]
#
#
#
#
# timed_alphas = [tf.new_alpha(1 + 3/ 12, 2 + 3/12, i) for i in np.arange(0, 1 + 1/3, 1/3)]
#
# params_list = [[timed_alphas[j], op.epsilon, tf.outbreak(ob_start, ob_end, ob_m, ramp_up=2/12, ramp_down=6/12)[0],
#                 tf.outbreak(ob_start, ob_end, ob_m, ramp_up=2/12, ramp_down=6/12)[1],
#                 tf.outbreak(ob_start, ob_end, ob_m, ramp_up=2/12, ramp_down=6/12)[2], op.zeta, op.delta, op.sigma, op.mu, op.mu_s] for j in
#                range(0, len(timed_alphas))]
#
#
#
# start = [1 + 3/12 for i in t]
# end = [2 + 3/12 for i in t]
#
# sol1 = op.ode_solver(t, op.initial_conditions, params_list[0])
# sol2 = op.ode_solver(t, op.initial_conditions, params_list[1])
# sol3 = op.ode_solver(t, op.initial_conditions, params_list[2])
# sol4 = op.ode_solver(t, op.initial_conditions, params_list[3])
#
# A0 = sol1[:, 2]
# A1 = sol2[:, 2]
# A2 = sol3[:, 2]
# A3 = sol4[:, 2]
#
# plt.figure()
# plt.plot(t, A0, label='lambda=0')
# plt.plot(t, A1, label='lambda=1/3')
# plt.plot(t, A2, label='lambda=2/3')
# plt.plot(t, A3, label='lambda=1')
# plt.plot(t, A, '--', label='No Outbreak')
# plt.xlim(50)
# # plt.ylim(bottom=4000)
# plt.plot(start, A3, 'g:', alpha=0.4, label="Lock-down Start")
# plt.plot(end, A3, 'r:', alpha=0.4, label="Lock-down End")
# plt.xlabel('Time (years)')
# plt.ylabel('Proportion of Population Addicted')
# plt.title('Lockdown Simulation for kappa = 3 from time 1 to 2')
# plt.legend()
# plt.show()
