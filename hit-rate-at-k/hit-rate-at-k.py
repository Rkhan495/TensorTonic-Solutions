def hit_rate_at_k(recommendations: list, ground_truth: list, k: int) -> float:
    """
    Returns the fraction of users with a relevant item in their first k recommendations.
    """
    hits = 0
    n = len(recommendations)
    if n == 0:
        return 0.0
    for user_recs, user_gt in zip(recommendations, ground_truth):
        top_k = user_recs[:k]
        if any(item in user_gt for item in top_k):
            hits += 1
            
    return hits / n