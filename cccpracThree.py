# fours and fives?
# inputVal = int(input())
# def fourFiver(numberCheck):
#     if numberCheck>4:
#         return 0
#     elif numberCheck==4:
#         return 1
#     elif numberCheck==5:
#         return 1
#     else:
#         counter = 0
#         total = 0
#         for val in range (int(numberCheck//4+1)):
#             total+=4
#             if total==numberCheck:
#                 counter+=1
#                 total=0
#             for val in range (int(numberCheck//5+1)):
#                 total+=5
#                 if total==numberCheck:
#                     counter+=1
#                     total=0
theNumber = int(input())
def fourFiver(numberCheck):
    count = 0
    for fourer in range (int(numberCheck//4+1)):
        remainder = numberCheck-(4*fourer)

        if remainder%5==0 and remainder>=0:
            count+=1
    return count

print (fourFiver(theNumber))