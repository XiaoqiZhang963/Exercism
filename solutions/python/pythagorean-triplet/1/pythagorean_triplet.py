def triplets_with_sum(n):
    triplets = []

    for a in range(1, n // 3 + 1):
        numerator = n * (n - 2 * a)
        denominator = 2 * (n - a)

        if numerator % denominator == 0:
            b = numerator // denominator
            c = n - a - b

            if a < b < c:
                triplets.append([a, b, c])

    return triplets