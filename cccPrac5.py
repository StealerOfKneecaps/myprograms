# the stupid fucking triangle problem

colNumbers = int(input())
laneOneColours = list( map( int, input().split() ) )
laneTwoColours = list( map( int, input().split() ) )


total = 0
for i in range (colNumbers):
    for row in range(2):
        if row == 0:
            current = laneOneColours
            other = laneTwoColours
        else:
            current = laneTwoColours
            other = laneOneColours
        
        if current[i]==1:
            length = 3
            if i>0 and current[i-1] ==1:
                length -=1
            if i<colNumbers-1 and current[i+1] ==1:
                length-=1
            if i%2==0 and other[i]==1:
                length-=1
            total +=length
            
print (total)