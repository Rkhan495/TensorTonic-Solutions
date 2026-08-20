import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    x = np.asarray(x, dtype=float)

    if x.ndim == 0:
        return x * (1/(1+np.exp(-x)))

    result = np.zeros_like(x)

    for index in np.ndindex(x.shape):
        result[index] = x[index] * (1/(1+np.exp(-x[index])))

    return result