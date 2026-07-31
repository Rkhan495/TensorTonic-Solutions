import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    result = 0.0

    for i in range(len(x)):
        result += np.abs(x[i] - y[i])

    return result