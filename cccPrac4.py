theGuysNeedSameGroup = int(input())
listSameGroup = []
for _ in range (theGuysNeedSameGroup):
    listSameGroup.append(input().split())

theGuysNeedDiffGroup = int(input())
listDiffGroup = []
for _ in range (theGuysNeedDiffGroup):
    listDiffGroup.append(input().split())

numOfGroups = int(input())
listGroups = {}
for i in range (numOfGroups):
    group = input().split()
    for groupmate in group:
        listGroups[groupmate]=i

total = 0
for needSameGroup in listSameGroup:
    if listGroups[needSameGroup[0]] != listGroups[needSameGroup[1]]:
        total +=1
for needDiffGroup in listDiffGroup:
    if listGroups[needDiffGroup[0]] == listGroups[needDiffGroup[1]]:
        total +=1
print (total)