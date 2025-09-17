import math
#uhhhhhhh it's the 17 of september also Reimu from touhou project
# def q1():
    #propgram that outputs factors of a number
#     factoredNumber = int(input("Yo what number you need factored da ze\n"))
#     factorCount = 0
#     for factor in range (1,factoredNumber+1):
#         if factoredNumber%factor == 0:
#             print(factor)
#             factorCount+=1
#     print (f"there are {factorCount} factors in {factoredNumber} yare yare da ze")
# q1()
#amog us
#What is this, some kind of for loop?
#say that again
#also do problem solving. what's lowest value, highest value, how to go about solving this stuff
#also this code kinda sucks it's SLOW SOOOOO change factoredNumber+1 to factoredNumber//2+1 because it's LINEAR COMPLEX ALGORITHm

def q1():
    factoredNumber = int (input("yo what number you need factored\t")) 
    factorCount = 0
    for factor in range(1,int(math.sqrt(factoredNumber)//1)):
        if factoredNumber%factor == 0:
            print(factor)
            print(int(factoredNumber/factor))
            factorCount+=2
    print (f"there are {factorCount} factors in {factoredNumber} yare yare da ze")
q1()