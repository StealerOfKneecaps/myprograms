# stupid ass clarinet problem

nmk = input()
n, m, k = nmk.split()
n = int(n)
m = int(m)
k = int(k)

def coolClarinetCompetition(n, m, k):
    listOfPossibleNumbers = []
    for value in range (1, m+1):
        listOfPossibleNumbers.append(value)
    