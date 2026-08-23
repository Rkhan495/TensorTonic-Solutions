import numpy as np

def selu(x, lam=1.0507009873554804934193349852946, alpha=1.6732632423543772848170429916717):
    """
    Apply SELU activation element-wise.
    Returns a list of floats rounded to 4 decimal places.
    """
    x = np.asarray(x, dtype=float)

    if x.ndim == 0:
        return x * lam if x > 0 else lam * alpha * (np.exp(x) - 1)

    result = np.zeros_like(x)

    for index in np.ndindex(x.shape):
        if x[index] > 0:
            result[index] = x[index] * lam
        else:
            result[index] = lam * alpha * (np.exp(x[index]) - 1)

    return result
