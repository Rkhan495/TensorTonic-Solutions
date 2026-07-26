def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    hits = sum(1 for i in recommended[:k] if i in relevant)
    return [(hits/k), (hits/len(relevant))]