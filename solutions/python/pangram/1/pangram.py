def is_pangram(sentence):
    sentence_letters = set(sentence.lower())
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if letter not in sentence_letters:
            return False
    return True
