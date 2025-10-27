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

# def bubobubobly (unSorte):
#     swap = True
#     while swap:
#         swap = False
#         for i in range (1, len(unSorte)):
#             if unSorte[i]<unSorte[i-1]:
#                 unSorte[i],unSorte[i-1] = unSorte[i-1],unSorte[i]
#                 swap = True
#     return unSorte
# print (bubobubobly([5,4,6,3,6,5,4,2]))
#This one is slightly better
#I'm gonna skibiditouchyou