#the fence problem

amtFences = int(input())
heights = list(map(int,input().split()))
lengths = list(map(int,input().split()))

sum = 0
for i in range(0, len(lengths)):
    sum+=lengths[i]*((heights[i]+heights[i+1])/2)
print (sum)