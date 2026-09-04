def translate(text):
    vowels = set('aeiou')
    pig_latin_list = []
    for word in text.split():
        pig_latin = ''
        if word[0] in vowels or word[0:2] in {'xr','yt'}:
            pig_latin = word +'ay'
        else:
            split = 0
            for index, letter in enumerate(word):
                if letter in vowels or (letter == 'y' and index>0):
                    split = index 
                    break
                elif word[index:index+2] == 'qu':
                    split = index + 2
                    break      
            pig_latin = word[split:] + word[:split] + 'ay'
        pig_latin_list.append(pig_latin)
    return ' '.join(pig_latin_list)
    
