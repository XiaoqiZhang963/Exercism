def is_armstrong_number(number):
    if not isinstance(number,int):
        raise TypeError("Number must be integer")
    number_str = str(number)
    power = len(number_str)

    total = 0
    for digit_str in number_str:
        digit = int(digit_str)
        total += digit**power
    return total == number
        
        
