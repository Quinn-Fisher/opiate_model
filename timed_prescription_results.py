import opiate_functions as op
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
import timed_functions as tf
import timeit
# a = tf.new_alpha(0, 5, 5)

#initial = [0.056, 0.0057, 0.0021, op.initN, 0.0057, 0.0056, 0]
# init_rates = [0.15, 0.00266, 0.0094, 0.00744]

cost_array = np.array(tf.p_control_sim(0, 1, 3, 6))
a = np.amin(cost_array)
b = np.amax(cost_array)
line1 = a + 0.25 * (b - a)
line2 = a + 0.5 * (b - a)
line3 = a + 0.75 * (b - a)

# Create plot
fig, ax = plt.subplots(figsize=(6, 6))
im = ax.imshow(cost_array, interpolation='none')
# Set ratio of x and y axis
ax.set_aspect(1)
# Create Contour lines for specific values and labels
_cs2 = ax.contour(cost_array, levels=[line1, line2, line3], colors=['white', 'red', 'magenta'],
                  alpha=0.65)

# Create and label notches on x and y axis
x_label_list = ['0', '0.25', '0.5', '0.75', '1']
y_label_list = ['0', '0.25', '0.5', '0.75', '1']
ax.set_xticks([0, 5, 10, 15, 20])
ax.set_yticks([0, 5, 10, 15, 20])
ax.set_xticklabels(x_label_list)
ax.set_yticklabels(y_label_list)
# plt.axis('off')
plt.xlabel('Start Time of Lockdown (years)')
plt.ylabel('Lockdown Level (lambda)')
plt.title('1 Year Outbreak ')
# Create cbar to show cost values

cbar = fig.colorbar(im, ax=ax, shrink=0.65)
cbar.add_lines(_cs2)
plt.show()

print(np.amin(cost_array), np.amax(cost_array), 1 - np.amin(cost_array) / np.amax(cost_array))

