t,n = map(int,input().split())
listStrings = []


for _ in range (t):
    s = input()
    freq = {}
    for chara in s:
        freq[chara]= freq.get(chara, 0) + 1
    
    valid = True
    
    for i in range(len(s)-1):
        if freq[s[i]]>1 and freq[s[i+1]]>1:
            valid = False
            break
        elif freq[s[i]]==1 and freq[s[i+1]]==1:
            valid = False
            break
    if valid:
        print("T")
    else:
        print("F")


