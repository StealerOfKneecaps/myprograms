# foursfive question
theNumber = int(input())
# 4a + 5b = theNumber
# 4a = theNumber - 5b
# a = (theNumber - 5b)/4
# look over all possible b so that it's divisible by 4, so all a and b are whole


sum = 0
for b in range(theNumber//5+1):
    if (theNumber-(5*b)/4)//1 == theNumber-(5*b)/4:
        sum+=1
print (sum)