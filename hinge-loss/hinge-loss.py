import numpy as np

def hinge_loss(y_true, y_score, margin=1.0, reduction="mean") -> float:
    """
    y_true: 1D array of {-1,+1}
    y_score: 1D array of real scores, same shape as y_true
    reduction: "mean" or "sum"
    Return: float
    """
    if len(y_true) != len(y_score):
        return
    result = []
    for i in range(len(y_true)):
        result.append(max(0, margin - (y_true[i] * y_score[i])))
    total = sum(result)
    if reduction == 'mean':
        return total / len(result)
    return total