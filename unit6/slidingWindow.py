s="aabbssredgfhyjgu"
tail=0
WS = ""
dic={}
res=0
for head in range(len(s)):
    WS += s[head]
    while s[head] in dic and dic[s[head]] > 0:
        res = max(res, head-tail)
        dic[s[tail]] -=1
        WS=WS[1:]
        tail+=1
    if s[head] in dic:
        dic[s[head]] +=1
    else:
        dic[s[head]] =1
print(max(res, head-tail))   
print(WS)
