PRESENTS = [("first","a Partridge in a Pear Tree"),("second","two Turtle Doves"),("third","three French Hens"),("fourth","four Calling Birds"),("fifth","five Gold Rings"),("sixth","six Geese-a-Laying"),("seventh","seven Swans-a-Swimming"),("eighth","eight Maids-a-Milking"),('ninth',"nine Ladies Dancing"),("tenth","ten Lords-a-Leaping"),("eleventh","eleven Pipers Piping"),("twelfth","twelve Drummers Drumming")]

def recite(start_verse, end_verse):
    lyrics = []
    
    for index in range(start_verse-1,end_verse):
        presents_list = [PRESENTS[i][1] for i in range(index,-1,-1)]
        
        if len(presents_list)>1:
            presents_list[-1] = "and " + presents_list[-1]
            
        lyrics_index = (f"On the {PRESENTS[index][0]} day of Christmas "
        f"my true love gave to me: {', '.join(presents_list)}.")
        
        lyrics.append(lyrics_index)
    return lyrics
    
