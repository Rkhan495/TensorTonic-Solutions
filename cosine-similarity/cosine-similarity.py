import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    dot_product = 0.0
    normA = 0.0
    normB = 0.0
    for i in range(len(a)):
        dot_product += (a[i] * b[i])
        normA += (a[i] ** 2)
        normB += (b[i] ** 2)

    normA = np.sqrt(normA)
    normB = np.sqrt(normB)

    if normA == 0 or normB == 0:
        return 0.0

    return dot_product / (normA * normB)
        