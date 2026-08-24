def target_encoding(categories: list, targets: list) -> list:
    """
    Returns each category replaced by its mean target.
    """
    sums = {}
    counts = {}

    for category, target in zip(categories, targets):
        if category not in sums:
            sums[category] = 0
            counts[category] = 0

        sums[category] += target
        counts[category] += 1

    means = {}

    for category in sums:
        means[category] = sums[category] / counts[category]

    return [float(means[category]) for category in categories]