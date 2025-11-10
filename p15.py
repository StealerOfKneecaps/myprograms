#For each numbe from 2 to N (user input) crate a key, value apir of its factors
def factor_finder(silksong):
    listylist = []
    for i in range(1,silksong+1):
        if silksong%i==0:
            listylist.append(i)
    return listylist
n = int(input("hey skibidi brochacho what is n"))
factornumber = {}
for i in range (1,n+1):
    factornumber[i] = factor_finder(i)
print (factornumber)