class Solution:
    # 오른쪽과 왼쪽 방향성을 잘 이용한 사례.
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        left_to_right, right_to_left = 1, 1
        res = [1] * n

        for i in range(n):
            res[i] *= left_to_right
            left_to_right *= nums[i]

            res[n-1-i] *= right_to_left
            right_to_left *= nums[n-1-i]

        return res
