class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r= max(piles)

        def helper(m):
            hour = sum([math.ceil(pile/m) for pile in piles ])

            return hour<=h

        while l<r:
            m = (l+r)//2

            if helper(m):
                r = m
            else:
                l = m+1
        return l

        