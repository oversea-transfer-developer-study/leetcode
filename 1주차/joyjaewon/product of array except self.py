'''
input - list[int]
output - list: each element is equal to the product of the remaining elements

Clarifications
- element can be negative or 0
- list is non-empty

Test Cases
[1,2,3,4] -> [24,12,8,6]
[0,1,2,3] -> [6,0,0,0]
[-1,-2,-3,-4] -> [-24,-12,-8,-6]

Approach 1) Brute Force - use double for loop to multiple the remaining elements. O(N^2)
Approach 2) use 2 lists to store prefix and postfix. 

Plan
- define the function taking the list as parameter
    - initialize left, right and result list
    - iterate over the array, store the multiplication of the left side in left
    - iterate over the array, store the multiplication of the right side in right
    - multiply corresponding elements from left and right, store the result in result
    - return result

[1,2,3,4]
left = [1, 1, 2, 6]
right = [24, 12, 4, 1]
result = [24, 12, 8, 6]     

TC: O(N), SC: O(N)
'''
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        left = [1] * n
        right = [1] * n
        result = [1] * n

        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
        
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        
        for i in range(n):
            result[i] = left[i] * right[i]
        
        return result