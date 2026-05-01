class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        have = 0 
        need = len(countT := Counter(t))
        countT = Counter(t)
        res,reslen = [-1,-1],float('inf')
        window = {}
        l = 0
        for r in range(len(s)):
            window[s[r]] = 1+ window.get(s[r],0)

            if window[s[r]] == countT.get(s[r],0) and s[r] in countT:
                have+=1
            
            while have==need:
                if reslen>r-l+1:
                    reslen = r-l+1
                    res = [l,r]
                
                window[s[l]]-=1
                if s[l] in t and window[s[l]] < countT[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if reslen!= float('inf') else ""
        





