import opiate_functions as op
import timed_functions as tf
import numpy as np
import matplotlib.pyplot as plt

cost_array = tf.p_control_death(0, 1, 3, 1, 5, a_cost=0, r_cost=0)

# Create plot
fig, ax = plt.subplots(figsize=(6, 6))
im = ax.imshow(cost_array, interpolation='none')
# Set ratio of x and y axis
ax.set_aspect(10)
# Create Contour lines for specific values and labels
_cs2 = ax.contour(cost_array, levels=[0.0278, 0.0282, 0.0285, 0.0287], colors=['white', 'pink', 'red', 'blue'])

# Create and label notches on x and y axis
x_label_list = ['0', '0.5', '1', '1.5', '2']
y_label_list = ['0', '0.25', '0.5', '0.75', '1']
ax.set_xticks([0, 10, 20, 30, 40])
ax.set_yticks([0, 5, 10, 16, 19])
ax.set_xticklabels(x_label_list)
ax.set_yticklabels(y_label_list)

# Create cbar to show cost values
cbar = fig.colorbar(im, ax=ax)
cbar.add_lines(_cs2)

# plt.xlabel('Initial Time of Prescription Lock-down (years)')
# plt.ylabel('Magnitude of Prescription Lock-Down (percentage of initial rate)')
# plt.title('Cost of 3-fold outbreak at month 0 until 1 years')
plt.show()