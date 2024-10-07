class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # temp1, 2 두개 써서도 풀었지만 좀 더 효율적인 방법으로는

        temp = []

        for j in range(len(nums)-1, -1, -1):
            if not temp: temp.append(nums[j])
            else: temp.append(temp[-1]+nums[j])

        temp = temp[::-1]
        
        temp_val = 0

        for i in range(len(nums)):
            temp_val += nums[i]
            if temp_val == temp[i]: return i

        return -1
