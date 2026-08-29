import numpy as np

def cross_entropy_loss(y_true: list[int], y_pred: list[list[float]]) -> float:
    """
    Returns the mean multiclass cross-entropy loss as a Python float.
    """
    L = []
    for i in range(len(y_true)):
        L.append(-np.log(y_pred[i][y_true[i]]))
    return np.mean(L) 