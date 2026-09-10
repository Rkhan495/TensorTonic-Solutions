def differencing(series: list, order: int) -> list:
    """
    Returns the series after the requested differencing order.
    """
    arr = series
    for i in range(order):
        curr = []
        for j in range(1, len(arr)):
            curr.append(arr[j] - arr[j-1])
        arr = curr
    return arr