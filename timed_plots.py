import opiate_functions as op
import timed_functions as tf
import numpy as np
import matplotlib.pyplot as plt

time = np.arange(1, 10, 0.5)

results1 = [(np.amax(tf.p_control_sim(0, 1, 3, 0.5, i)) - np.amin(tf.p_control_sim(0, 1, 3, 0.5, i))) * 100000 for i in time]
results2 = [(np.amax(tf.p_control_sim(0, 1, 3, 1, i)) - np.amin(tf.p_control_sim(0, 1, 3, 0.5, i))) * 100000 for i in time]
results3 = [(np.amax(tf.p_control_sim(0, 1, 3, 1.5, i)) - np.amin(tf.p_control_sim(0, 1, 3, 0.5, i))) * 100000 for i in time]
results4 = [(np.amax(tf.p_control_sim(0, 1, 3, 2, i)) - np.amin(tf.p_control_sim(0, 1, 3, 0.5, i))) * 100000 for i in time]


plt.plot(time, results1, '--bo', label='0.5 Year Lockdown')
plt.plot(time, results2, '--ro', label='1 Year Lockdown')
plt.plot(time, results3, '--go', label='1.5 year Lockdown')
plt.plot(time, results4, '--co', label='2 Year lockdown')
plt.xlabel('Time (years)')
plt.ylabel('Optimum Addiction Years Saved per 100k people')
plt.title('Optimal Lockdown results 1 Year 3-Fold Outbreak')
plt.legend()
plt.show()
