import math

def poisson_pmf_cdf(lam: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    current_pmf = math.exp(-lam)
    cdf = current_pmf
    pmf = current_pmf
    
    # Use recurrence to accumulate probabilities up to k
    for i in range(1, k + 1):
        current_pmf = current_pmf * lam / i
        cdf += current_pmf
        if i == k:
            pmf = current_pmf
            
    return {
        "pmf": float(pmf),
        "cdf": float(cdf)
    }