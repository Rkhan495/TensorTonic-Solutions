import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    x = np.asarray(x)
    pmf = np.zeros(len(x))
    for i in range(len(x)):
        if x[i] == 1:
            pmf[i] = p
        else:
            pmf[i] = 1-p
    var = p * (1 - p)
    return (pmf, p, var)