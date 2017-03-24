# Author: Jake VanderPlas
# License: BSD
#   The figure produced by this code is published in the textbook
#   "Statistics, Data Mining, and Machine Learning in Astronomy" (2013)
#   For more information, see http://astroML.github.com
#   To report a bug or issue, use the following forum:
#    https://groups.google.com/forum/#!forum/astroml-general

import numpy as np
from scipy.stats import binom
from matplotlib import pyplot as plt

# ----------------------------------------------------------------------
# This function adjusts matplotlib settings for a uniform feel in the textbook.
# Note that with usetex=True, fonts are rendered with LaTeX.  This may
# result in an error if LaTeX is not installed on your system.  In that case,
# you can set usetex to False.
from astroML.plotting import setup_text_plots

setup_text_plots(fontsize=8, usetex=True)

# ------------------------------------------------------------
# Define the distribution parameters to be plotted
n_values = [255, 255]
b_values = [1.0 / 6]
linestyles = ['-']
x = np.arange(-1, 200)

# ------------------------------------------------------------
# plot the distributions
fig, ax = plt.subplots(figsize=(5, 3.75))

for (n, b, ls) in zip(n_values, b_values, linestyles):
    # create a binomial distribution
    dist = binom(n, b)

    plt.plot(x, dist.pmf(x), ls=ls, c='black',
             label=r'$b=%.1f,\ n=%i$' % (b, n), linestyle='steps-mid')

plt.xlim(-0.5, 256)
plt.ylim(0, 0.2)

plt.xlabel('$x$')
plt.ylabel(r'$p(x|b, n)$')
plt.title('Binomial Distribution')

plt.legend()
plt.show()
