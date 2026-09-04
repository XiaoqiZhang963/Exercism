def encode(plain_text):
    cleaned = ''.join(character.lower() for character in plain_text if character.isalnum())
    encode_list = []
    for letter in cleaned:
        if letter.isalpha():
            letter_encode = chr(ord('z')-(ord(letter)-ord('a')))
        else:
            letter_encode = letter
        encode_list.append(letter_encode)
        
    encode_str = ''.join(encode_list)
    return ' '.join(encode_str[i:i+5] for i in range(0, len(encode_str),5))
        


def decode(ciphered_text):
    cleaned = ciphered_text.replace(' ','')
    return ''.join([chr(ord('a')+(ord('z')-ord(letter))) if letter.isalpha() else letter for letter in cleaned])
