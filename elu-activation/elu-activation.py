import numpy as np

def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    result = x

    for i in range(len(x)):
        if x[i] <= 0:
            result[i] = alpha * (np.exp(x[i]) - 1)
            
    return result