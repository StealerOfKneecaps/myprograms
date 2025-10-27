#INSERTI MERTI PERTI
#iterates, sorts from bottom one element at a time
#If an element is greater than the left element(s), then it's sorted - otherwise put it where it belongs (swap it with elements until it's sorted)
def quality_deutsche_efficiency(owo):
    i = 1
    while i < len(owo):
        j=i
        while j>0:
            if owo[j-1]>owo[j]:
                owo[j-1],owo[j]=owo[j],owo[j-1]
            else:
                break #since everything to the left is guaranteed to be already sorted
            j-=1
        i+=1
    return owo

def sort_it(listyA, listyB):
    #where A and B are connected. 
    swap = True
    while swap:
        swap = False
        for i in range (1, len(listyA)):
            if listyA[i-1]>listyA[i]:
                listyA[i-1], listyA[i] = listyA[i], listyA[i-1]
                listyB[i-1], listyB[i] = listyB[i], listyB[i-1]
                swap = True
    return listyA,listyB

print(sort_it([3, 5, 2, 4, 1, 6],[9, 25, 4, 16, 1, 36]))