def maximizer(amtTime, totalChores, listyTime):
    listy = sorted(listyTime)
    i=0
    total = 0
    while i<len(listy):
        if total+listy[i]<=amtTime:
            total+=listy[i]
            i+=1
        else:
            break
    return i





totalTime = int(input("Hey bro"))
amtChorse = int(input("yo"))

timeListy = []
for _ in range(amtChorse):
    timeListy.append(int(input("sup")))
print (maximizer(totalTime,amtChorse,timeListy))