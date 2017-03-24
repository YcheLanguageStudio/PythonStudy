from scipy import stats
import scipy
from scipy.stats import distributions

import numpy as np


def binom_test(x, n=None, p=0.5, alternative='two-sided'):
    print x, n, p , alternative
    """
    Perform a test that the probability of success is p.

    This is an exact, two-sided test of the null hypothesis
    that the probability of success in a Bernoulli experiment
    is `p`.

    Parameters
    ----------
    x : integer or array_like
        the number of successes, or if x has length 2, it is the
        number of successes and the number of failures.
    n : integer
        the number of trials.  This is ignored if x gives both the
        number of successes and failures
    p : float, optional
        The hypothesized probability of success.  0 <= p <= 1. The
        default value is p = 0.5

    Returns
    -------
    p-value : float
        The p-value of the hypothesis test

    References
    ----------
    .. [1] http://en.wikipedia.org/wiki/Binomial_test

    """
    x = scipy.atleast_1d(x).astype(np.integer)
    if len(x) == 2:
        n = x[1] + x[0]
        x = x[0]
    elif len(x) == 1:
        x = x[0]
        if n is None or n < x:
            raise ValueError("n must be >= x")
        n = np.int_(n)
    else:
        raise ValueError("Incorrect length for x.")

    if (p > 1.0) or (p < 0.0):
        raise ValueError("p must be in range [0,1]")

    if alternative not in ('two-sided', 'less', 'greater'):
        raise ValueError("alternative not recognized\n"
                         "should be 'two-sided', 'less' or 'greater'")

    if alternative == 'less':
        pval = distributions.binom.cdf(x, n, p)
        return pval

    if alternative == 'greater':
        pval = distributions.binom.sf(x - 1, n, p)
        return pval

    # if alternative was neither 'less' nor 'greater', then it's 'two-sided'
    d = distributions.binom.pmf(x, n, p)
    rerr = 1 + 1e-7
    if x == p * n:
        # special case as shortcut, would also be handled by `else` below
        pval = 1.
    elif x < p * n:
        i = np.arange(np.ceil(p * n), n + 1)
        y = np.sum(distributions.binom.pmf(i, n, p) <= d * rerr, axis=0)
        pval = (distributions.binom.cdf(x, n, p) +
                distributions.binom.sf(n - y, n, p))
    else:
        i = np.arange(np.floor(p * n) + 1)
        y = np.sum(distributions.binom.pmf(i, n, p) <= d * rerr, axis=0)
        pval = (distributions.binom.cdf(y - 1, n, p) +
                distributions.binom.sf(x - 1, n, p))

    return min(1.0, pval)


print scipy.stats.binom_test(51, 235, 1.0 / 6, alternative='greater')
print binom_test(51, 235, 1.0 / 6, alternative='greater')
