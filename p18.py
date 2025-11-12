def missing_no_finder(skibilist):
    limit = len(skibilist)
    freq_table = {}
    for x in skibilist:
        freq_table[x] = 1
    for i in range (0, limit+1):
        if i not in freq_table:
            return i
    return -1
print (missing_no_finder([3, 1, 5, 6, 2, 4, 8, 0, 9]))