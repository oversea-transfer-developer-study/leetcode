class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # 아래의 솔루션은 pop이 있으므로 O(n**2).

        # zero_cnt = 0
        # i = 0

        # while i < len(nums):    
        #     if not nums[i]:
        #         nums.pop(i)
        #         zero_cnt += 1
        #     else: i += 1

        # while zero_cnt:
        #     zero_cnt -= 1
        #     nums.append(0)

        left = 0

        for right in range(len(nums)):
            if nums[right]:
                nums[right], nums[left] = nums[left], nums[right]

                print(left, right, nums)

                left += 1
