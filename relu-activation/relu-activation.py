import numpy as np

def relu(x):
    x = np.asarray(x)

    if x.ndim == 0:
        return x if x > 0 else 0

    result = np.zeros_like(x)

    for index in np.ndindex(x.shape):
        if x[index] > 0:
            result[index] = x[index]

    return result