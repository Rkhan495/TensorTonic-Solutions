def binning(values: list, num_bins: int) -> list:
    """
    Returns the equal-width bin index of every value.
    """
    min_val = min(values)
    max_val = max(values)

    if min_val == max_val:
        return [0] * len(values)

    w = (max_val - min_val) / num_bins

    result = []

    for value in values:
        index = int((value - min_val) / w)

        if index >= num_bins:
            index = num_bins - 1

        result.append(index)

    return result