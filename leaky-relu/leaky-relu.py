import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    result = np.zeros(len(x))
    for i in range(len(x)):
        if x[i] >= 0:
            result[i] = x[i]
        else:
            result[i] = x[i] * alpha

    return result