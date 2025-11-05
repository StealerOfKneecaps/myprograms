listopolis = [1, 1, 2, 3, 4, 5, 6, 9] #always sorted
def isItSkibidiRizz(a, silksong):
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