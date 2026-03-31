#INSERTI MERTI PERTI
#iterates, sorts from bottom one element at a time
#If an element is greater than the left element(s), then it's sorted - otherwise put it where it belongs (swap it with elements until it's sorted)
def quality_deutsche_efficiency(owo):
    i = 1
    while i < len(owo):
        j=i
        while j>0:
            if owo[j-1]>owo[j]:
                owo[j-1],owo[j]=owo[j],owo[j-1]
            else:
                break #since everything to the left is guaranteed to be already sorted
            j-=1
        i+=1
    return owo
def quality_skibidi_refirerirenre(uwu):
    for i in range(0, len(uwu)):
         for j in range (i, 0, -1):
            if uwu[j-1]>uwu[j]:
                uwu[j-1],uwu[j]=uwu[j],uwu[j-1]
            else:
                break
    return uwu
print(quality_skibidi_refirerirenre([5, 3, 2, 2, 7, 8, 1, 9, 0]))