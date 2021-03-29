from typing import Any, Union

import opiate_functions as op
import numpy as np
import matplotlib.pyplot as plt
import scipy as sc


new_params = [op.params[i] for i in range(0, 10)]
new_params[0] = [0.00125 * 0.8 for i in np.arange(0, op.t_max, 1)]

cost1 = op.addiction_cost(5000000, op.initial_conditions, op.params, 1)
cost2 = op.addiction_cost(5000000, op.initial_conditions, new_params, 1)

print(cost1 - cost2)
