import opiate_functions as op
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
import timed_functions as tf

# settings
h, w = 10, 10  # for raster image
nrows, ncols = 4, 4  # array of sub-plots
figsize = [10, 15]  # figure size, inches

# # prep (x,y) for extra plotting on selected sub-plots
# xs = np.linspace(0, 2*np.pi, 60)  # from 0 to 2pi
# ys = np.abs(np.sin(xs))           # absolute of sine


# img_array = np.array([[tf.p_control_sim(0, 1, i, j, 1.5, a_cost=1, r_cost=0) for i in np.arange(3, 4, 1)]
#                       for j in np.arange(0, 2, 1)])

# create figure (fig), and array of axes (ax)
fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)

# plot simple raster image on each sub-plot
for i, axi in enumerate(ax.flat):
    # i runs from 0 to (nrows*ncols-1)
    # get indices of row/column
    rowid = i // ncols
    colid = i % ncols
    # axi is equivalent with ax[rowid][colid]
    img = tf.p_control_sim(0, 1, 1 + i / 4, 5)
    axi.imshow(img, vmin=0.03978866371458232, vmax=0.050465160504637986, cmap='gray')
    # axi.imshow(img)
    axi.axis('off')


    # write row/col indices as axes' title for identification
    #axi.set_title('O.B. len = ' + str(i / 2 + 1))


plt.show()

