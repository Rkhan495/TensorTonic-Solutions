import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    count = 0
    if len(set(y_true)) == 1:
        for i in range(len(y_true)):
            if y_true[i] == y_pred[i]:
                count += 1
                if count == len(y_true):
                    return 1.0
        return 0.0

    mean = sum(y_true) / len(y_true)
    SStot = 0
    SSres = 0

    for i in range(len(y_true)):
        SStot += ((y_true[i] - mean) * (y_true[i] - mean))
        SSres += ((y_true[i] - y_pred[i]) * (y_true[i] - y_pred[i]))
    
    return 1 - (SSres / SStot)