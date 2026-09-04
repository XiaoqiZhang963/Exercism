def is_isogram(phrase):
    seen = set()

    for char in phrase.lower():
        if not char.isalpha():
            continue
        if char in seen:
            return False
        seen.add(char)

    return True
