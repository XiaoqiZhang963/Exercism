def egg_count(display_value):
    binary = bin(display_value)[2:]
    return sum([int(num) for num in binary])
