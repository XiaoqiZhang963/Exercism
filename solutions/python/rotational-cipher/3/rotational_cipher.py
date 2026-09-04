def rotate(text, key):
    rotated_list = []
    
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            letter_index = ord(char) - base
            shifted_index = (letter_index + key)%26
            char_rotated = chr(shifted_index + base)
        else:
            char_rotated = char
        rotated_list.append(char_rotated)

    return ''.join(rotated_list)
        
