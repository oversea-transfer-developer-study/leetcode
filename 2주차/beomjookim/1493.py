class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        res = 0
        used = False

        for r in range(len(nums)):
            if not nums[r]:
                if used:
                    while nums[l]: l += 1
                    l += 1
                else: used = True
            
            if res < r-l+1: res = r-l
        
        return res
