import math
#I'm not explaining this because you can't read
def finder(numArg):
    sum = 0
    for i in range (1, math.floor(math.sqrt(numArg)+1)):
        if numArg%i==0:
            sum += i
            sum += numArg/i #I give up optimising bro
    if sum==numArg:
        return True
    else:
        return False
for i in range (1, 1000001):
    if finder(i)==True:
        print (f"{i} is a perfect number")