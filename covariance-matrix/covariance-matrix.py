import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    X = np.array(X)
    if X.ndim != 2:
        return None

    
    n = len(X)
    length = len(X[0])
    result = []
    means = []

    if n < 2:
        return None

    for row in X:
        if len(row) != length:
            return None

    for j in range(length):
        col_sum = 0
        for i in range(n):
            col_sum += X[i][j]
        means.append(col_sum / n)

    for i in range(length):
        row = []
        for j in range(length):
            cov = 0
            for k in range(n):
                cov += (X[k][i] - means[i]) * (X[k][j] - means[j])

            cov /= (n-1)
            row.append(cov)

        result.append(row)

    return np.array(result)