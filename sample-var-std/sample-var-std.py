import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    x = np.array(x)
    n = len(x)
    if n < 2:
        return
    mean = np.mean(x)

    var = sum((x - mean) ** 2) / (n - 1)
    std = np.sqrt(var)
    return (var, std)