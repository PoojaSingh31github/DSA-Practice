def lengthOfLongestSubstring(s):
    first =0
    second =0
    lenn=0
    count=[0]*256
    while second < len(s):
        while count[ord(s[second])]:
            count[ord(s[first])] = 0
            first +=1
        count[ord(s[second])] =1
        lenn = max(lenn, second - first + 1)
        second +=1  
    return lenn  


s = "abcabcbb"
print(lengthOfLongestSubstring(s))      
        