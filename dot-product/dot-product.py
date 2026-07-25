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


'''
DEEP-ML Solution
import numpy as np

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    b = np.zeros((len(a[0]), len(a)), dtype=type(a))

    for i in range(len(a[0])):
        for j in range(len(a)):
            b[i,j] = a[j][i]

    return b
'''
*/
