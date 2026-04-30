class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s =="":
            return 0
        temp = set()
        i = 0 
        maxlen = 1
        for j in range(len(s)):
            while (s[j] in temp):
                temp.remove(s[i])
                i+=1
                
            maxlen = max(maxlen,j-i+1)
            temp.add(s[j])
        return maxlen
        