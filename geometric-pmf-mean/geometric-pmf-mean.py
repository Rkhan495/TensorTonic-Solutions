import numpy as np

def geometric_pmf_mean(k: list, p: float) -> dict:
    """
    Returns a dictionary with pmf and mean.
    """
    k = np.asarray(k)
    pmf = (1 - p) ** (k-1) * p
    
    return {'pmf': pmf, 'mean': 1.0/p}