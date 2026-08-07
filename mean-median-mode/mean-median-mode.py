import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    n = len(x)
    total = 0.0
    for i in range(n):
        total += x[i]
    mean = total / n

    x = np.sort(x)
    median = 0.0
    if n % 2 != 0:
        median = x[((n+1) // 2) - 1]
    else:
        median = (x[(n//2)-1] + x[n//2]) / 2

    counts = Counter(x)
    max_freq = max(counts.values())
    modes = [num for num, freq in counts.items() if freq == max_freq]
    mode = min(modes)

    return mean, median, mode
        

    

    