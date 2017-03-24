from scipy.integrate import quad
import numpy as np
from scipy.stats import *


def chi2_pdf(x):
    return chi2.pdf(x, df=1)


ans0, err0 = quad(norm.pdf, 0.6, np.inf)
ans1, err1 = quad(chi2_pdf, 0.6, np.inf)

print ans0, err0
print ans1, err1
