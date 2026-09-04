def top_k_recommendations(scores: list, rated_indices: list, k: int) -> list:
    """
    Returns the highest-scoring unrated item indices.
    """
    rated_set = set(rated_indices)
    
    unrated_items = [
        (score, idx) for idx, score in enumerate(scores) 
        if idx not in rated_set
    ]
    
    unrated_items.sort(reverse=True, key=lambda x: x[0])
    
    return [idx for score, idx in unrated_items[:k]]