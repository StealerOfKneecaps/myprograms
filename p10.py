#a clean
def paleKing(text):
    text = text.strip()
    result = ""
    for ind in range (0,len(text)):
        if text[ind].isalpha(): #true if character is alphabetical
            result = result + text[ind].lower()
    return result
'''
let X represent a string, T be a target character to search
let I represent index of a strring
while i<len(x), if x[i] == T then return i else i + 1
if T is not foundm return -1
'''

def strLinSearch(text, target):
    if not text:
        return -1
    i=0
    while i<len(text):
        if text[i]==target:
            return i
        else:
            i+=1
    return -1
print (strLinSearch("The pale king did nothing wrong", "k"))
