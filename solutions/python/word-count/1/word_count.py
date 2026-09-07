def count_words(sentence):
    words_dict = {}
    current_word = ""
    for char in sentence:
        if char.isalnum() or char == "'":
            current_word += char.lower()
        elif current_word:
            word = current_word.strip("'")
            if word:
                words_dict[word] = words_dict.get(word,0) + 1
            current_word = ""
    if current_word:
        word = current_word.strip("'")
        if word:
            words_dict[word] = words_dict.get(word,0) + 1

    return words_dict
        
