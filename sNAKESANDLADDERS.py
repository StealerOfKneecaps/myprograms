print("Hello! this is a snakesandladder simulator. Input your dicerolls!")
win = False
currentPos = 0
while (win==False):
    diceRoll = int(input("Yo what's your diceroll (honour system guys)\n"))
    if diceRoll>12 or diceroll<2:
        print("NIce try bozo")
    else:
        if currentPos+diceRoll<=100:
            currentPos+=diceRoll
        gameDict = {
            3:34,
            54:19,
            40:64,
            90:48,
            67:86,
            99:77
        }
        if currentPosition in gameDict:
            currentPosition = gameDict[currentPosition]
        elif currentPos+diceRoll>100:
            print("reroll, highr than 100")
        elif currentPos == 100: 
            win=True
            print("YOU WON YOU GIGACHAD SIGMA TOUHOU PROJECT!!!!!!")
        print(f"current position is {currentPos}")

#use a switchcase p