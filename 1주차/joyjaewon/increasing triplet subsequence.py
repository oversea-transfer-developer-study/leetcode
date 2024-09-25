'''
input: list 
output: boolean - true if there exists a triplet where nums[i] < nums[j] < nums[k]

Clarifications
- length of the list can be less than 3
- number can be negative
- there can be multiple valid cases
- triplet doesn't have to be next to each other

Test Cases
[1,2,3,4,5] -> true
[5,4,3,2,1] -> false
[1,2] -> false
[1,-1,2,-2,3] -> true (1,2,3)

Approach 1) use triple for-loop to check each combinations O(N^3)
Approach 2) use double for-loop + two pointer O(N^2)
Approach 3) one pass. try to find three numbers in the increasing order. 
            If the third number is found, return True

Plan
- define the function taking the list as parameter
    - handle edge case: if the length of the list is less than 3, return False
    - initialize first and second to float('inf')
    - iterate over the list
        - if the current number is less than first, update first
        - elif the current number is lees than second, update second
        - else, return True (this means we found the number first < second < third)
    - return False

TC: O(N), SC: O(1)
'''
class Solution:
    def increasingTriplet(self, nums):
        if len(nums) < 3:
            return False
        
        first = float('inf')  
        second = float('inf') 
        
        for num in nums:
            if num <= first:
                first = num  
            elif num <= second:
                second = num  
            else:
                return True
        
        return False