def primes(limit):
    unmarked = set(range(2,limit+1))

    for num in range(2,limit+1):
        if num in unmarked:
            for multiple in range(num*2, limit+1, num):
                unmarked.discard(multiple)
                
    return list(unmarked)
