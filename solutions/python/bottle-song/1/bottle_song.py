NUMBER = ['no','one','two','three','four','five','six','seven','eight','nine','ten']

def recite(start, take=1):
    if take > start + 1:
        raise ValueError
        
    lyrics = []
    
    for num in range(start,start-take,-1):
        bottle = 'bottle' if num == 1 else 'bottles'
        first = NUMBER[num].capitalize() + " green " + bottle + " hanging on the wall,"

        bottle = 'bottle' if num-1 == 1 else 'bottles'
        last = "There'll be " + NUMBER[num-1] + " green " + bottle + " hanging on the wall."
        
        lyrics.extend([first, first, "And if one green bottle should accidentally fall,", last])

        if num != start - take + 1:
            lyrics.append('')
            
    return lyrics
        
