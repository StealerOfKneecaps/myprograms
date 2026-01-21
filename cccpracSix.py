# the dumbass shitty neighbour's stupid fucking fence
N = int(input())
I = input()
T = input()
listHeights = []
for element in I.split():
    listHeights.append(int(element))
for element in T.split():
    listWidths.append(int(element))

squareas = []
j=0
i=0
while j<len(listWidths):
    while i<len(listHeights)-1:
        squareas.append(width*(min(listHeights[i],listHeights[i+1])))
        i+=1
        j+=1
