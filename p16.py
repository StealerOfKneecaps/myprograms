def ana_recur(tou, hou):
#     dictTou={}
#     dictHou={}
#     tou = tou.lower()
#     tou = tou.replace(" ","")
#     hou = hou.lower()
#     hou = hou.replace(" ","")
#     i=0
#     for charaNumOne in range (0, len(tou)):
#         for charaNum in range (0,len(tou)):
#             if tou[charaNum]==tou[charaNumOne] and charaNum!=charaNumOne:
#                 i+=1
#         dictTou[tou[charaNumOne]] = i
#         i=0
#     j=0
#     for charaNumTwo in range (0, len(hou)):
#         for charaNumThree in range (0, len(hou)):
#             if hou[charaNumTwo]==hou[charaNumThree] and charaNumTwo!=charaNumThree:
#                 j+=1
#         dictHou[hou[charaNumTwo]] = j
#     return dictHou==dictTou
# print (ana_recur("anagram","nag a ram")) 
# TS DOESN"T WORK becaus eI counted too many tims
    freq_table = {}
    for c in tou:
        if c in freq_table:
            freq_table[c]+=1
        else:
            freq_table[c]=1
    for d in hou:
        if d not in freq_table:
            return False
        else:
            freq_table[d]-=1
            if freq_table[d]<0:
                return False
    for key, value in freq_table.items():
        if value!=0:
            return False
    return True
#This frequency table is better