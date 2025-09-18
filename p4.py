# import random
# #self explanatory
# def main():
#     shouldStop = "n"
#     while shouldStopOrNo != "y":
#         shouldStop = "n"
#         userInput = (input("guess h for heads and t for tails. Call it!").strip()).lower()
#         headsOrTails = random.randint(0,1)
#         if (userInput=="h" and headsOrTails==1) or (userInput=="t" and headsOrTails==0):
#             print("YAyyyyyy you wONNNNN you must be blessed by REIMU from TOUHOU PROJECT")
#         else:
#             print("lmao loser")
#         shouldStopOrNo = (input("Wanna play again? y/n").strip()).lower()

# def actualMain():
#     playAgain = "y"
#     while (playAgain == "y"):
#         while True:
#             headTailInput = input((("Heads or tails! Call it.\n").lower()).strip())
#             if headTailInput in {"head","tail","heads","tails","h","t"}: #a list btw
#                 break
#             else:
#                 print ("idiot type in heads or tails ")
#         headsOrTails = random.randint(0,1)
#         if (headsOrTails==1 and headTailInput in {"head","heads","h"}) or (headsOrTails==0 and headTailInput in {"tail","tails","t"}):
            
#             print("Holy shit you're a fucking genius you're blessed by reimu touhou project probably")
#             print(f"also the computer generated {headsOrTails}")
#         else:
#             print("dumb moron")
#             print(f"also the computer generated {headsOrTails}")
#         playAgain = input("also do you want to play again y/n I'll assume everything other than y is no\n")

#immutability: datatype or an object that can not mutate. Strings are immutable becasue we can't make them cahnge self
#we need to re-update after we do something like .lower()