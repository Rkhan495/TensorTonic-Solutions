import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """

    x = np.asarray(x, dtype=float)

    if x.ndim == 0:
        if x >= 0:
            e = np.exp(-2 * x)
            return (1 - e) / (1 + e)
        else:
            e = np.exp(2 * x)
            return (e - 1) / (e + 1)

    result = np.zeros_like(x)

    for index in np.ndindex(x.shape):
        value = x[index]

        if value >= 0:
            e = np.exp(-2 * value)
            result[index] = (1 - e) / (1 + e)
        else:
            e = np.exp(2 * value)
            result[index] = (e - 1) / (e + 1)

    return result