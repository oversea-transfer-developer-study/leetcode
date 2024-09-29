# 1. Problem 
# You are given an array flowerbed representing a garden bed, where flowerbed[i] = 0 means the spot is empty, and flowerbed[i] = 1 means the spot is occupied by a flower

	
# 2. Test case
# 		Input: flowerbed = [1,0,0,0,1], n = 1
# 		Output: true
		
# 		Input: flowerbed = [1,0,0,0,1], n = 2
# 		Output: false
		
#     Input: flowerbed = [0, 0, 0, 0, 0], n = 2
#     Output: true 

	
# 3. Plan
# 	loop each spot
# 	if current spot is empty, check the previous one and the next within the range
	
	
# Time Complexity: O(n)
# Space Complexity: O(1)

count = 0
length = len(flowerbed)
    
for i in range(length):
    if flowerbed[i] == 0:
        empty_prev = (i == 0) or (flowerbed[i - 1] == 0)
        empty_next = (i == length - 1) or (flowerbed[i + 1] == 0)
            
        if empty_prev and empty_next:
            count += 1  
            flowerbed[i] = 1  
                
            if count >= n:
                return True
    
return count >= n
 
