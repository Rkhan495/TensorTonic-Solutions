import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    # total = 0.0
    
    # x_len = len(x)
    # y_len = len(y)
    # max_len = max(x_len, y_len)

    # for i in range(max_len):
    #     if i < x_len and i < y_len:
    #         total += (x[i] - y[i]) ** 2
    #     elif i < x_len:
    #         total += x[i] ** 2
    #     elif i < y_len:
    #         total += y[i] ** 2

    return np.sqrt(np.sum((x - y) ** 2))