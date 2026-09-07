def sum_of_multiples(limit, bases):
    multiples = set()
    for num in range(limit):
        for base in bases:
            if base>0 and num%base == 0:
                multiples.add(num)
                break
                
    return sum(multiples)
