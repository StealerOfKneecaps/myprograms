import math
dATA = [2,3,3,6,5,9,10,100,14,17]
j = 0
for d in dATA:
    j+=d
print(j/len(dATA))

swapped = True
while swapped:
    swapped = False
    for i in range (1, len(dATA)):
        if dATA[i]<dATA[i-1]:
            dATA[i],dATA[i-1]=dATA[i-1],dATA[i]
            swapped = True

if len(dATA)%2==1:
    print(dATA[int(len(dATA)//2)])
else:
    print ((dATA[int(len(dATA)/2)-1]+dATA[int(len(dATA)/2)] )/2)