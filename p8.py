#fibonoonono sequence

#0, 1, 1, 2, 3, 5, 8, 13

def nthFibNumber(n):
    if n in {0, 1}:
        return n
    else:
        return nthFibNumber(n-1) + nthFibNumber(n-2)
#comments more like... dumb... lmao gottem
nInput = int(input("Hey bro which fib u want me to find bro\n"))
nFound = nthFibNumber(nInput)
print (f"the fib numb at {nInput} is {nFound}")