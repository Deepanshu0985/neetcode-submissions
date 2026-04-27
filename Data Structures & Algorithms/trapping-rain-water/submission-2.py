class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxL = height[0]
        maxR = height[n-1]
        ans = 0
        l = 0
        r = n-1

        while l<r:
            if height[l]<height[r]:
                ans+= max(0,maxL-height[l])
                maxL = max(maxL,height[l])
                l+=1
            else:
                ans+= max(0,maxR-height[r])
                maxR = max(maxR,height[r])
                r-=1
        return ans

        