
def silkSong(listy, value):
    length = len(listy)
    n = length//2
    val = listy[n-1]
    j=n//2
    while val!=value:
        if val>value:
            n//=2
            j=n//2
            val = listy[n-1]
        else:
            n+=j
            j//=2
            val = listy[n-1]
    return n
def binary(silk, song):
    low = 0
    high = len(silk)
    while low<high:
        silksong = (low+high)//2
        if silk[silksong]==song:
            return silksong
        elif silk[silksong]>song:
            high = silksong
        else:
            low = silksong
    return -1