class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1 = ''.join(sorted(s1))

        for i in range(len(s2) - n + 1):
            if s1 == ''.join(sorted(s2[i:i+n])):
                return True
        return False