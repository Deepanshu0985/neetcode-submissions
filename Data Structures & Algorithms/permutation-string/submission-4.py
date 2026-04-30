class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)

        if m>n:
            return False
        
        freq1 = [0]*26
        freq2 = [0]*26

        for ch in s1:
            freq1[ord(ch)-ord('a')]+=1
        
        i = j =0
        while j<n:
            freq2[ord(s2[j]) - ord('a')]+=1

            if j-i+1 > m:
                freq2[ord(s2[i])-ord('a')]-=1
                i+=1
            
            if freq1==freq2:
                return True
            j+=1
        return False
