import numpy as np

def vector_norm_3d(v: list) -> float | np.ndarray:
    """
    Returns a float or a NumPy array.
    """
    v = np.asarray(v, dtype=float)
    if v.ndim == 1:
        return np.sqrt(np.sum(v ** 2))
    result = []
    for i in v:
        result.append(np.sqrt(np.sum(i**2)))
    return np.asarray(result)