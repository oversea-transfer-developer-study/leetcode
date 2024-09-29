# 1. Problem 
# finding the product of the remaining elements except each element in a given arrangement

# 2. Test case
# 	Input: nums = [1,2,3,4]
#   Output: [24,12,8,6]: 
			
#   Input: nums = [5, 3, 4, 2]
#   Output: [24, 40, 30, 60]
		
	
# 3. Plan
# 1) Initialize Two Passes for Left and Right Products
# 2) Calculate Left Products
# 3) Calculate Right Products and return Result
  
# Time Complexity: O(n)
# Space Complexity: O(1)

def productExceptSelf(nums):
    n = len(nums)
    # Step 1: Initialize the result array with 1s
    answer = [1] * n
    
    # Step 2: Calculate left products
    left_product = 1
    for i in range(n):
        answer[i] = left_product
        left_product *= nums[i]
    
    # Step 3: Calculate right products and finalize result
    right_product = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right_product
        right_product *= nums[i]
    
    return answer


