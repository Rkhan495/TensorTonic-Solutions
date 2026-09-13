def mean_rating_imputation(ratings_matrix: list, mode: str) -> list:
    """
    Returns a copy with missing ratings replaced by user or item means.
    """
    result = [row[:] for row in ratings_matrix]

    rows = len(ratings_matrix)
    cols = len(ratings_matrix[0])

    if mode == "user":
        for i in range(rows):
            total = 0
            count = 0

            for j in range(cols):
                if ratings_matrix[i][j] != 0:
                    total += ratings_matrix[i][j]
                    count += 1

            mean = total / count if count > 0 else 0.0

            for j in range(cols):
                if result[i][j] == 0:
                    result[i][j] = mean

    else: 
        for j in range(cols):
            total = 0
            count = 0

            for i in range(rows):
                if ratings_matrix[i][j] != 0:
                    total += ratings_matrix[i][j]
                    count += 1

            mean = total / count if count > 0 else 0.0

            for i in range(rows):
                if result[i][j] == 0:
                    result[i][j] = mean

    return result