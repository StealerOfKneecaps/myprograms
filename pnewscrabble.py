def pointCounter(word):
    val1 = "aeioulnstr"
    val2 = "dg"
    val3 = "bcmp"
    val4 = "fhvwy"
    val5 = "k"
    val8 = "jx"
    val10 = "qz"
    point = 0
    for chara in word:
        if chara in val1:
            point+=1
        elif chara in val2:
            point+=2
        elif chara in val3:
            point +=3
        elif chara in val4:
            point+=4
        elif chara in val5:
            point+=5
        elif chara in val8:
            point+=8
        else:
            point+=10
    return point
def scrabobble(hornetsilksong):
    wordValMap = {}
    for val in hornetsilksong:
        wordValMap[val]=pointCounter(val)
    return wordValMap
print(scrabobble(["paleking","hornetsilksong","lacesilksong","reimutouhou"]))