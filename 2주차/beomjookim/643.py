class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        temp = sum(nums[:k])
        res = temp
        i = 0

        while i < len(nums)-k:
            temp -= nums[i]
            temp += nums[i+k]

            if res < temp: res = temp

            i += 1
        
        return res/k
