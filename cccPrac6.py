totalPeople = int(input())

hatList = []
for _ in range(totalPeople):
    hatList.append(int(input()))

total = 0
for i in range (len(hatList)):
    if hatList[i]==hatList[int(i+(totalPeople)//2)%totalPeople]:
        total+=1
print (total)