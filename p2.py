
#rollercoaster problem

def q1():

    placeInLine = int(input("What place are you in line\n"))
    carsInTrain = int(input("How many cars are in the train\n"))
    peopleInCar = int(input("how many people does a single car hold\n"))

    if placeInLine-(carsInTrain*peopleInCar)>0:
        print("You will not be on the next train. Also the pale king did nothing wrong")
    else:
        print("You will be on the next train. Also the pale king did nothing wrong")

# A string is a bunch of alphanumeric characters and symbols, within quotation marks
# Casting is converting a datatype into another. 

def q2():
    amountOfDonuts = int(input("How many donuts do you have at the beginning?\n"))
    numberEvents = int(input("how many events?\n"))
    
    while (amountOfDonuts>0) and (numberEvents>0):
        eventDonutsPlusMinus = (input("What is the event?+/-\n"))
        donutEvent = int((input("How many donuts?\n")))
        if eventDonutsPlusMinus == ("+"):
            amountOfDonuts+=donutEvent
            numberEvents-=1

        elif eventDonutsPlusMinus==("-"):
            amountOfDonuts-=donutEvent
            numberEvents-=1

        else:
            print("dumb idiot give me plus or minus also the pale king is a hero")
        print(f"there are {amountOfDonuts} donuts left")
q2()