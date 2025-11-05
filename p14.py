def scrabble_point_counter(silksong):

    silksong = silksong.lower()
    dictPoints = {
        "a": 1, "e": 1, "i": 1, "l": 1, "n": 1, "o": 1, "r": 1, "s": 1, "t": 1, "u": 1,
        "d": 2, "g": 2,
        "b": 3, "c": 3, "m": 3, "p": 3,
        "f": 4, "h": 4, "v": 4, "w": 4, "y": 4,
        "k": 5,
        "x": 8, "j": 8,
        "q": 10, "z": 10
    }
    sum = 0
    for chara in silksong:
        sum+=dictPoints[chara]
    return sum

def list_score_storer(songsilk):
    score_list = []
    for elem in songsilk:
        score_list.append(scrabble_point_counter(elem))
    return score_list

def bubobbly (silk,song):
    swap = True
    while swap:
        swap = False
        for i in range (1,len(song)):
            if song[i]>song[i-1]:
                song[i],song[i-1]= song[i-1],song[i]
                silk[i],silk[i-1]= silk[i-1],silk[i]
                swap=True
    return silk
word_list = ["lace","silksong","hornet","paleking"]
points = list_score_storer(word_list)
print (bubobbly(word_list,points))
print(points)