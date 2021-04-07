import numpy as np
import opiate_functions as op
import timed_functions as tf
import matplotlib.pyplot as plt

t_total = 1.5

l_start = 0
l_end = 1
l_level = np.arange(0, 1.05, 0.05)

ob_start = 0
ob_end = 1
ob_m = [2, 2.5, 3, 3.5]

h = 1e-5

S = []

for j in [0, 1, 2, 3]:
    z = [np.amin(tf.p_control_sim(ob_start, ob_end, ob_m[j], l_level[i], t_total)) for i in range(0, len(l_level))]
    z_p = [np.amin(tf.p_control_sim(ob_start, ob_end, ob_m[j], l_level[i] + h, t_total)) for i in range(0, len(l_level))]
    z_m = [np.amin(tf.p_control_sim(ob_start, ob_end, ob_m[j], l_level[i] - h, t_total)) for i in range(0, len(l_level))]

    S_j = [((z_p[i] - z_m[i]) / (2 * h)) * (l_level[i] / z[i]) for i in range(0, len(l_level))]

    S.append(S_j)


plt.plot(l_level, S[0], "o", label='2-Fold Outbreak')
plt.plot(l_level, S[1], "o",  label='2.5-Fold Outbreak')
plt.plot(l_level, S[2], "o",  label='3-Fold Outbreak')
plt.plot(l_level, S[3], "o", label='3.5-Fold Outbreak')
plt.xlabel('Nominal Lockdown Level')
plt.ylabel("Sensitivity")
plt.title('Sensitivity of Optimal Lockdown at Values of Lockdown Length')
plt.show()
