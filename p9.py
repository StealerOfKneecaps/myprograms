#Stringy
#determine a palindrome!
def isPalin(word):
    return word == word[::-1]
wordChecked = input("bro what word you want me to check if palindr\n")
if isPalin(wordChecked):
    print("yeah bro it's a pladrnoew")
else:
    print("nah bro it's not a padlinf ")