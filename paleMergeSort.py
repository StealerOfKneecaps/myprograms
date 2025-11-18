#comparison based, classified as "divide and conquer" algorithm
#2 implementation - bottom up,  top down
#complexity: o(n log n) worst case performance
#make "sorting 1 million numbres" seem trivial by dividing it and stuff
#n log in since diving half, half half but then n for the rest of the operations
#divide in half hafl half half and combines the smallest noes in pairs that are created
#have unsorted, divide until it becomes simple eough to sort. THen we combine, combine combine...

def mergeSort(tuhuList):
    #the splitter
    #base case
    if len(tuhuList)>=1:
        return tuhulist
    #work towards the base case
    middle = len(tuhuList)//2
    left = tuhuList[:middle]
    right = tuhuList[middle:]

    left = mergeSort(left)
    right = mergeSort(right)
    return combine(left,right)
def combine(left,right)
    #the combiner
    #assumed that left and right are both sorted
    if len(left)==0 and len(right)==0:
        return []
    elif len(left)==0:
        return right
    elif len(right)==0:
        return left
    else:
        i=0
        j=0
        answer = []
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                answer.append(left[i])
                i+=1
            else:
                answer.append(right[j])
                j+=1
        while i<len(left):
            answer.append(left[i])
            i+=1
        while j<len(right):
            answer.append(right[j])
    return answer
    