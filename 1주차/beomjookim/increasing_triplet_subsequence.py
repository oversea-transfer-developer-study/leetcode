class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # 왼 -> 오 가면서 그 수 이전 가장 작은 수를 비교해주기. T/F로
        # 오 -> 왼 가면서 그 수 이전 가장 큰 수를 비교해주기. T/F로

        res = []
        min_left = float('inf')
        max_right = float('-inf')

        for i in range(len(nums)):
            res.append(nums[i] > min_left)
            if min_left > nums[i]: min_left = nums[i]
        
        for j in range(len(nums)-1,-1,-1):
            if res[j] and max_right > nums[j]: return True
            if max_right < nums[j]: max_right = nums[j]

        return False
