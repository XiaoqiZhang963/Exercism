def is_valid(isbn):
    isbn = isbn.replace('-','')
    
    if len(isbn)!=10:
        return False

    if not isbn[:9].isdigit():
        return False

    if not (isbn[9].isdigit() or isbn[9] == 'X'):
        return False
        
    total = 0
    for index, digit in enumerate(isbn):
        if digit.isdigit():
            total += int(digit)*(10-index)
        else:
            total += 10*(10-index)
            
    return total%11 == 0
        
        
