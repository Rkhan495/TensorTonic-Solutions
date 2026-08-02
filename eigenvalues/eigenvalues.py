import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    try:
        matrix = np.asarray(matrix)
        if matrix.ndim <= 2 and matrix.shape[0] != matrix.shape[1] :
            return None
    except:
        return None

    eigenvals = np.linalg.eigvals(matrix)

    np.lexsort(eigenvals)

    return eigenvals
    