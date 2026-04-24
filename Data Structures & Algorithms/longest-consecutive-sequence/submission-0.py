class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        last = float('-inf')
        currcnt = 1
        ans = 0
        nums.sort()

        for i in range(len(nums)):
            if nums[i]==last:
                continue
            
            if nums[i]-1==last:
                currcnt+=1
            else:
                currcnt = 1
            ans = max(currcnt,ans)
            last = nums[i]
        return ans



        