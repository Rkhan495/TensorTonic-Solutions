def catalog_coverage(recommendations: list, n_items: int) -> float:
    """
    Returns the fraction of catalog items that were recommended.
    """
    if n_items == 0:
        return 0.0

    flat_recs = []
    for item in recommendations:
        if isinstance(item, list):
            flat_recs.extend(item)
        else:
            flat_recs.append(item)
            
    return len(set(flat_recs)) / n_items