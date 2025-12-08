import math
totalDist = int(input())
totalUses = int(input())
smallDist = []
for _ in range(totalUses):
    smallDist.append(int(input()))


def golfer(bigDist, clubs):
    distances = [0]+[math.inf]*bigDist
    for current in range(len(distances)):
        for c in clubs:
            new_location = current+c
            if new_location <=bigDist:
                distances[new_location] = min(distances[current]+1,distances[new_location])
    return distances[bigDist]
