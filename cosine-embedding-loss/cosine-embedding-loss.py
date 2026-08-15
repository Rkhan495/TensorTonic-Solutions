import numpy as np

def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    dot_product = 0.0
    normA = 0.0
    normB = 0.0
    for i in range(len(x1)):
        dot_product += (x1[i] * x2[i])
        normA += (x1[i] ** 2)
        normB += (x2[i] ** 2)

    normA = np.sqrt(normA)
    normB = np.sqrt(normB)

    cosine = dot_product / (normA * normB)

    if label == 1:
        return 1 - cosine
    return max(0, cosine - margin)