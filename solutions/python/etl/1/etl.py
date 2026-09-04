def transform(legacy_data):
    updated_data = {}
    for point, letter_list in legacy_data.items():
        letter_list = [letter.lower() for letter in letter_list]
        updated_data.update(dict.fromkeys(letter_list,point))
    updated_data = dict(sorted(updated_data.items()))
    return updated_data
