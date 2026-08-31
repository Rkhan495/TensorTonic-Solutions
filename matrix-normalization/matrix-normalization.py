import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    matrix = np.array(matrix, dtype=float)
    
    if norm_type == 'l1':
        divisor = np.sum(np.abs(matrix), axis=axis, keepdims=True)
    elif norm_type == 'l2':
        divisor = np.sqrt(np.sum(matrix ** 2, axis=axis, keepdims=True))
    else:
        divisor = np.max(np.abs(matrix), axis=axis, keepdims=True)
        
    return np.where(divisor == 0, 0.0, matrix / divisor)