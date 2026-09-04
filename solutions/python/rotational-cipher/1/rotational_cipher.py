def rotate(text, key):
    original = 'abcdefghijklmnopqrstuvwxyz'
    rotated = original[key:] + original[:key]

    text_rotated = ''
    for tx in text:
        letter = tx.lower()
        if letter in original:
            index = original.find(letter)
            letter_rotated = rotated[index]
            if letter == tx:
                text_rotated += rotated[index]
            else:
                text_rotated += rotated[index].upper()
        else:
            text_rotated += letter

    return text_rotated
        
