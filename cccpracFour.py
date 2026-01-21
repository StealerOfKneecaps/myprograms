# the weird ass shitty problem
must = []
cant = []

X = int(input())
for _ in range(X):
    a, b = input().split()
    must.append((a, b))

Y = int(input())
for _ in range(Y):
    a, b = input().split()
    cant.append((a, b))

groups = {}
G = int(input())
for groupID in range(G):
    a,b,c = input().split()
    groups[a]=groupID
    groups[b]=groupID
    groups[c]=groupID

violations = 0
for a,b in cant:
    if groups[a]==groups[b]:
        violations+=1

for a,b in must:
    if groups[a]!=groups[b]:
        violations+=1
