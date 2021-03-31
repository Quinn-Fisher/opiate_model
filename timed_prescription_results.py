import opiate_functions as op
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
from matplotlib import cm
import timed_functions as tf
import time as time
from scipy.interpolate import griddata

# set up initial conditions
initial = [0.15, 0.02, 0, 1, 0.02, 0]

# Set outbreak conditions and "lock-down" length
ob = 3  # multiplicative of addiction rates
ob_start = 0  # years
ob_end = 1  # years
lock_len = 1

cost_time = 2

cost_array = []

for i in np.arange(0, 1, 0.02):
    timed_alpha = [tf.new_alpha(j, j + lock_len, i) for j in np.arange(0, cost_time, 0.01)]

    params_list = [
        [timed_alpha[j], op.epsilon, tf.outbreak(ob_start, ob_end, ob)[0], tf.outbreak(ob_start, ob_end, ob)[1],
         tf.outbreak(ob_start, ob_end, ob)[2], op.zeta, op.delta, op.sigma, op.mu, op.mu_s] for j in
        range(0, len(timed_alpha))]

    cost_list = [op.con_cost(np.arange(0, cost_time, op.dt), initial, params_list[j], 1, 0, population=100000) for j in
                 range(0, len(params_list))]

    cost_list = np.array(cost_list)

    cost_array.append(cost_list)

cost_array = np.array(cost_array)

fig, ax = plt.subplots(figsize=(6, 6))
im = ax.imshow(cost_array, interpolation='none')
ax.set_aspect(4)
_cs2 = ax.contour(cost_array, levels=[6100, 6150, 6200, 6240], colors=['white', 'pink', 'red', 'blue'])

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
plt.title('Cost of 3-fold outbreak at month 0 for 0.5 years')
plt.show()

print(cost_array.shape)
