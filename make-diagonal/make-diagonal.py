import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    n = len(v)
    result = np.zeros((n, n))
    for i in range(n):
        result[i][i] = v[i]
    return result
