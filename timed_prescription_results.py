import opiate_functions as op
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
import timed_functions as tf
import time

# set up initial conditions
initial = [0.056, 0.0057, 0.0021, op.initN, 0.0057, 0.0056]
init_rates = [0.15, 0.00266, 0.0094, 0.00744]
cost_array = tf.p_control_sim(0, 0.5, 3, 1, 2, initial, init_rates)


fig, ax = plt.subplots(figsize=(6, 6))
im = ax.imshow(cost_array, interpolation='none')
ax.set_aspect(2)
_cs2 = ax.contour(cost_array, levels=[2325, 2375, 2425, 2475], colors=['white', 'pink', 'red', 'blue'])

x_label_list = ['0', '0.5', '1', '1.5', '2']
y_label_list = ['0', '0.25', '0.5', '0.75', '1']
ax.set_xticks([0, 50, 100, 150, 200])
ax.set_yticks([-0.5, 12, 24.5, 37, 49.5])
ax.set_xticklabels(x_label_list)
ax.set_yticklabels(y_label_list)

cbar = fig.colorbar(im, ax=ax)
cbar.add_lines(_cs2)

plt.xlabel('Initial Time of Prescription Lock-down (years)')
plt.ylabel('Magnitude of Prescription Lock-Down (percentage of initial rate)')
plt.title('Cost of 3-fold outbreak at month 0 until 1 years')
plt.show()

# Set outbreak conditions and "lock-down" length
# ob = 3  # multiplicative of addiction rates
# ob_start = 0  # years
# ob_end = 1  # years
# lock_len = 1
#
# cost_time = 2
#
# cost_array = []
# print(time.time())
# for i in np.arange(0, 1, 0.02):
#     timed_alpha = [tf.new_alpha(j, j + lock_len, i) for j in np.arange(0, cost_time, 0.01)]
#
#     params_list = [
#         [timed_alpha[j], op.epsilon, tf.outbreak(ob_start, ob_end, ob)[0], tf.outbreak(ob_start, ob_end, ob)[1],
#          tf.outbreak(ob_start, ob_end, ob)[2], op.zeta, op.delta, op.sigma, op.mu, op.mu_s] for j in
#         range(0, len(timed_alpha))]
#
#     cost_list = [op.con_cost(np.arange(0, cost_time, op.dt), initial, params_list[j], 1, 1) for j in
#                  range(0, len(params_list))]
#
#     cost_list = np.array(cost_list)
#
#     cost_array.append(cost_list)
#
# cost_array = np.array(cost_array)
# print(time.time())

