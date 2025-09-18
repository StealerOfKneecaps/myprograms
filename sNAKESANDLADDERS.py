print("Hello! this is a snakesandladder simulator. Input your dicerolls!")
win = False
currentPos = 0
while (win==False):
    diceRoll = int(input("Yo what's your diceroll (honour system guys)\n"))
    if diceRoll>12:
        print("NIce try bozo")
    else:
        if currentPos+diceRoll<=100:
            currentPos+=diceRoll
        else:
            print("reroll, highr than 100")
        if currentPos == 9:
            currentPos = 34
        elif currentPos == 54:
            currentPos = 19
        elif currentPos == 40:
            currentPos = 64 
        elif currentPos == 90:
            currentPos = 48
        elif currentPos == 67:
            currentPos = 86
        elif currentPos == 99:
            currentPos = 77 
        elif currentPos == 100: #seeing the elifs makes my eyes cry
            win=True
            print("YOU WON YOU GIGACHAD SIGMA TOUHOU PROJECT!!!!!!")
        print(f"current position is {currentPos}")

    