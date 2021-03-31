import opiate_functions as op
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
from matplotlib import cm
import timed_functions as tf
# set up initial conditions
initial = [0.15, 0.02, 0, 1, 0.02, 0]

# Set outbreak conditions and "lock-down" length
ob = 3  # multiplicative of addiction rates
ob_start = 0  # years
ob_end = 0.5  # years
lock_len = 0.5
cost_time = 2


cost_array = []

for i in np.arange(0, 1, 0.02):

    timed_alpha = [tf.new_alpha(j, j + lock_len, i) for j in np.arange(0, cost_time, 0.01)]

    params_list = [
        [timed_alpha[j], op.epsilon, tf.outbreak(ob_start, ob_end, ob)[0], tf.outbreak(ob_start, ob_end, ob)[1],
         tf.outbreak(ob_start, ob_end, ob)[2], op.zeta, op.delta, op.sigma, op.mu, op.mu_s] for j in range(0, len(timed_alpha))]

    cost_list = [op.con_cost(np.arange(0, cost_time, op.dt), initial, params_list[j], 1, 0) for j in
                 range(0, len(params_list))]

    cost_list = np.array(cost_list)

    cost_array.append(cost_list)

cost_array = np.array(cost_array)

fig, ax = plt.subplots(figsize=(6, 6))
ax.imshow(cost_array, interpolation='none', extent=[0, cost_time, 1, 0])
ax.set_aspect(2)

ax = plt.gca()  # get the current axes
for PCM in ax.get_children():
    if isinstance(PCM, cm.ScalarMappable):
        break

plt.colorbar(PCM, ax=ax)
plt.xlabel('Initial Time of Prescription Lock-down (years)')
plt.ylabel('Magnitude of Prescription Lock-Down (percentage of initial rate)')
plt.title('Cost of 3-fold outbreak at month 0 for 0.5 years')
plt.show()
