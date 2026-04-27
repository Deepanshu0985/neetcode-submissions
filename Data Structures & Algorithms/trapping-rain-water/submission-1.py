class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0]*len(height)
        suffix = [0]*len(height)
        prefix[0] = height[0]
        suffix[len(height)-1] = height[len(height)-1]
        for i in range(1,len(height)):
            prefix[i] = (max(height[i],prefix[i-1]))

        for i in range(len(height)-2,-1,-1):
            suffix[i] = (max(height[i],suffix[i+1]))

        print(prefix)
        print(suffix)

        ans = 0
        for i in range(len(height)):
            if min(prefix[i],suffix[i])>0:
                ans+= min(prefix[i],suffix[i]) - height[i]
        
        return ans
        
        