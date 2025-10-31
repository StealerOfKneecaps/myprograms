#listylist? 
#problem 1
num = int(input("brosephinben I\'m gonna print the list of even numbers from 2 to oooyour nunmber"))
listy = list(range(2, num+1, 2))
print (listy)

#problem 2
#given array of integers, output true i 6 appears as the first or last element in the array
def is_six_first_or_last(thing):
    if thing[0]==6 or thing[-1]==6:
        return True
    return False