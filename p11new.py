#Create an empty list
listylist = []

#determine if a tring is empty
if not listylist:
    print("empt")

#what does len(), sum(), min(), max() do when list is an arg
listy = [3,1,4,1,5,9]
print(len(listy))
print(sum(listy))
print(min(listy))
print(max(listy))

#accss individuial character/item in a list
#access first, acces last items
toehoes = list("Aya", "Sanae", "mistr00s")
print toehoes[0]
print toehoes[0:2]


#join two/multiple lists together
bests = ["Moors", "rems", "skukuys"]
worsts = ["Remillia","sunny milk"]
bests.extend(worsts)
for item in worsts:
    bests.append(item)

#reverse a list
print bests.reverse()

#create a copy of a lsit


#compare lists for equal

#determine if an item exists within a list

# locate the index of an item in a list

#count how often an item occurs within a list

#convert a string to a list

#sort a list

#sort two lists where the index are attache to each otehr 