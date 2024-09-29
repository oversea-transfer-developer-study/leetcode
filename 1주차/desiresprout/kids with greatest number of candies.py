# 1. Problem 
# You are given an array candies where each element represents the number of candies each child has. You are also given an integer extraCandies, which represents the number of extra candies you can give to each child. 


# 2. Test case
# 	Input: candies = [2,3,5,1,3], extraCandies = 3
# 	Output: [true,true,true,false,true] 
	
# 	Input: candies = [4,2,1,1,2], extraCandies = 1
# 	Output: [True, False, False, False, False]
	
# 3. Plan
# 	The simplest approach is to first find the maximum number of candies any child currently has. 
# 	Then, for each child, check if adding extraCandies to their current number of candies would make their total greater than or equal to this maximum.
	
	
# Time Complexity: O(N)
# Space Complexity: O(N)

max_candies = max(candies)
result = []
for candy in candies:
    result.append(candy + extraCandies >= max_candies)
    
return result
	
