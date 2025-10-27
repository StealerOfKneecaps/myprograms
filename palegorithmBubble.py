#BUBBLE SORT
def bubbly(notSorted):
    for _ in notSorted:
        i = 0
        for _ in range (1, len(notSorted)):
            if notSorted[i]>notSorted[i+1]:
                notSorted[i],notSorted[i+1] = notSorted[i+1],notSorted[i]
            i+=1
    return notSorted
print (bubbly([5, 5, 5, 3, 5, 5, 4, 5, 5, 5, 4, 1, 2]))