def moving_median(values: list, window_size: int) -> list:
    """
    Returns the median of every complete sliding window.
    """
    if window_size == 1:
        return values

    result = []

    for i in range(len(values) - window_size + 1):
        window = values[i:i + window_size]
        window.sort()

        n = len(window)

        if n % 2 == 1:
            median = window[n // 2]
        else:
            median = (window[n // 2 - 1] + window[n // 2]) / 2

        result.append(float(median))

    return result