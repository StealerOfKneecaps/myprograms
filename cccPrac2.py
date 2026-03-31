# weird painting problem
rowNumbers = int(input())
colNumbers = int(input())
numberChanges = int(input())

listChanges = []
for _ in range(numberChanges):
    listChanges.append(input().split())

rows = rowNumbers*[0]
cols = colNumbers*[0]


i = 0
while i < len(listChanges):
    if listChanges[i][0] == "R":
        rows[int(listChanges[i][1])-1]^=1
    else:
        cols[int(listChanges[i][1])-1]^=1
    i+=1

rowsToggledOddTimes = sum(rows)
colsToggledOddTimes = sum(cols)

sum = rowsToggledOddTimes*(colNumbers-colsToggledOddTimes)+colsToggledOddTimes*(rowNumbers-rowsToggledOddTimes)
print (sum)


