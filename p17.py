
def expon_recursive(a,b):
    if b==0:
        return 1
    elif b==1:
        return a
    else:
        return a*(expon_recursive(a,b-1))
print(expon_recursive(2,5))