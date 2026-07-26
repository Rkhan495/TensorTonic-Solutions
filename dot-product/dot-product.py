import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    
    a = np.array(x)
    b = np.array(y)

    if a.ndim != 1 or b.ndim != 1:
        raise ValueError("Arrays should be 1-dimnesional")

    if a.shape[0] != b.shape[0]:
        raise ValueError("Length of both arrays should be same")

    return float(np.dot(a, b))
