def rows(letter):
    n = ord(letter) - ord('A')
    result = []

    for i in range(n + 1):
        char = chr(ord('A') + i)
        outer = ' ' * (n - i)

        if i == 0:
            line = outer + char + outer
        else:
            inner = ' ' * (2 * i - 1)
            line = outer + char + inner + char + outer

        result.append(line)

    return result + result[-2::-1]
