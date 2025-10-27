#Selection sort. ALGORITHM!!!! we did this one already

#always use a function
def selection_sorter(unsortedList):
    if len(unsortedList)<=1: #mild optimisation
        return unsortedList
    else:
        i = 0
        #hunt for smallest value
        while i < len(unsortedList):
            smallest = unsortedList[i]
            j = i+1
            newLocation = i

            while j < len(unsortedList):
                newValue = unsortedList[j]

                if newValue<smallest:
                    smallest = newValue
                    newLocation = j
                j+=1
            
            #swap smallest value
            
            unsortedList[i],unsortedList[newLocation] = unsortedList[newLocation], unsortedList[i]
            i+=1
    return unsortedList
print(selection_sorter([5, 6, 2, 7, 9, 1, 3, 0, 4, 8]))
