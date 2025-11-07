listopolis = [1, 1, 2, 3, 4, 5, 6, 9] #always sorted
def isItSkibidiRizz(a, silksong): #The super duper one (the fastest)
    begin = 0
    end = len(a)-1
    while begin<end:
        if a[begin]+a[end]==silksong:
            return True
        elif a[begin]+a[end]>silksong:
            end-=1
        else:
            begin+=1
    return False
print (isItSkibidiRizz(listopolis,6))

#bruteforcemethod
def the_handmaids_tale_by_margaret_atwood(laceSilksong, hornetSilksong):
    for i in range(0,len(laceSilksong)):
        for j in range(0,len(laceSilksong)):
            if laceSilksong[i]+laceSilksong[j]==hornetSilksong and i!=j:
                return True
    return False
print(the_handmaids_tale_by_margaret_atwood(listopolis,6))

#def  linearsearch

def linse(eee,fff):
    for i in range(0, len(eee)-1):
        diff = fff-eee[i]
        for j in range (i+1,len(eee)):
            if eee[j]==diff:
                return True
    return False
print(linse(listopolis,6))