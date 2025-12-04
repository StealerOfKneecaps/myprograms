#rearrange zero to end
def zero_rearranger(silksong):
    i = 0
    thingLen = len(silksong)
    while i < thingLen:
        if silksong[i]==0:
            silksong.pop(i)
            silksong.append(0)
            thingLen-=1
        else:
            i+=1
    return silksong
def other_solution (hollowknight): #list of zeros as a placeholder
    temp = [0]*len(hollowknight)
    i=0
    for hollow in hollowknight:
        if hollow!=0:
            temp[i] = hollow
            i+=1
    hollowknight=temp
    return hollowknight

def best_solution (zoteboat):
    zero_i=0
    for i in range(len(zoteboat)):
        if zoteboat[i]!=0:
            zoteboat[i],zoteboat[zero_i] = zoteboat[zero_i],zoteboat[i]
            zero_i+=1
    return zoteboat
    #zero_i doesn't go up if it's a zero, but i does and when it eventually isn't zero it swaps
    #uses less memory