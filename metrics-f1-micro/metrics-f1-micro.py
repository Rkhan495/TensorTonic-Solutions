def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    tptn, fpfn = 0, 0
    for i in range(len(y_true)):
        if y_true[i] == y_pred[i] :
            tptn += 1
        elif y_true[i] != y_pred[i]:
            fpfn += 1 
    return (tptn / (tptn + (0.5 * (fpfn+fpfn))))
