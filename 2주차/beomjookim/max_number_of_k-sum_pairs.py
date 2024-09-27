from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = Counter(nums)
        res = 0
        already = set([])

        for key in nums:
            if 2*key < k:
                if k-key in nums and key not in already and k-key not in already:
                    res += min(nums[key], nums[k-key])
                    already.add(k-key)
                    already.add(key)
                    
            elif 2*key == k: res += nums[key]//2

        return res
