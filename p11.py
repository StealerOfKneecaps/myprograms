def cleanerUpper(thingy): 
    upper = "" 
    positive = ""
    negatives = ""
    sum = 0
    for chara in thingy:
        if chara.isalpha() and item.isupper():
            upper+=chara
            if len(positives)>0:
                sum+=int(positives)
                positives = ""
            if len(negatives) > 0:
                sum+= int(negatives)
                negatives = ""
        elif chara == "-":
            if len(negatives) > 0:
                sum+= int(negatives)
                negatives = "-"
            else:
                negatives = "-"
        elif item.isdigit():
            if len(negatives)> 0:
                negatives += item
            else:
                positives += item
    if len(postives)>0:
        sum += int(positives)

    if len(negatives)>0:
        sum += int(negatives)

    product_code = upper + str(sum)
    return product_code
    