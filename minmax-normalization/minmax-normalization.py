import numpy as np

def minmax_scale(x, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    x = np.array(x, dtype=float)
    if len(x.shape) > 2:
        return
        
    xmin = np.min(x, axis=axis, keepdims=True)
    xmax = np.max(x, axis=axis, keepdims=True)
    diff = xmax - xmin
    diff = np.where(diff == 0, eps, diff)
    return (x - xmin) / diff