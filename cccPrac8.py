string = input()
indexToFind = int(input())

listedString = []
letter = ""
total = ""
for ind in range(len(string)):
    if ind = 0:
        listedString.append([])
    if not string[ind].isdigit():
        letter = string[ind]
        listedString.append([letter,int(total)])
        total = ""
        letter = ""
    else:
        total += string[ind]

leng = 0
for j in listedString:
    leng+=j[1]
indexToFind%=leng
for i in range (len(listedString)):
    if indexToFind<listedString[i][1]:
        print (listedString[i][0])
        break