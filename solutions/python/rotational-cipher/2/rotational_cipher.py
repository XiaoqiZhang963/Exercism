def rotate(text, key):
    rotated_list = []
    for char in text:
        char_rotated = ''
        if char.islower():
            letter_index = ord(char) - ord('a')
            shifted_index = (letter_index + key)%26
            char_rotated = chr(shifted_index + ord('a'))
        elif char.isupper():
            letter_index = ord(char) - ord('A')
            shifted_index = (letter_index + key)%26
            char_rotated = chr(shifted_index + ord('A'))
        else:
            char_rotated = char
        rotated_list.append(char_rotated)

    return ''.join(rotated_list)
        
