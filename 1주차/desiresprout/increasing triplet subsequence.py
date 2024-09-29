# 1. Problem 
# an unsorted array of integers nums. The task is to determine if there exists an increasing triplet subsequence in the array

# 2. Test case
# 	Input: nums = [1,2,3,4,5]
#   Output: true
			
#   Input: nums = [5, 3, 4, 2]
#   Output: [24, 40, 30, 60]
		
	
# 3. Plan
#  Initialize two variables representing the smallest and second smallest values
#  Iterate list
#  update first to be the smallest number
#  update second to be the second smallest number
#  Found a number greater than both first and second, hence triplet exists

  
# Time Complexity: O(n)
# Space Complexity: O(1)

def increasingTriplet(nums):
    if len(nums) < 3:
        return False
    
    first = float('inf')
    second = float('inf')
    
    for n in nums:
        if n <= first:
            first = n  
        elif n <= second:
            second = n  
        else:
            return True
    
    return False


