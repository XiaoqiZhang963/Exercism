def find_letters(word):
    letters = {}
    for char in word.lower():
        letters[char] = letters.get(char,0) + 1
    return letters

def find_anagrams(word, candidates):
    word_lower = word.lower()
    target = find_letters(word)
    
    return [candidate for candidate in candidates if find_letters(candidate) == target and candidate.lower() != word_lower]
    
