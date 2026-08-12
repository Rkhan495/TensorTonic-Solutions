import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    if len(x) != len(p):
        raise ValueError("Length not match")

    if sum(p) != 1:
        raise ValueError("Probability is not 1")

    value = 0
    for i in range(len(x)):
        value += x[i] * p[i]

    return value