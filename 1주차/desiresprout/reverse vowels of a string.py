# 1. Problem 
# Given a string s, reverse only the vowels of the string and return the modified string. The vowels are a, e, i, o, u, both in lowercase and uppercase forms (A, E, I, O, U)
	

# 2. Test case
# 		Input: the sky is blue
# 		Output: blue is sky the
			
# 		Input: "  hello world  "
# 		Output: world hello

	
# 3. Plan
# 	iterate over the string to find the positions of the vowels.
# 	use two pointer approach
	
	
# Time Complexity: O(n)
# Space Complexity: O(n)


vowels = set("aeiouAEIOU")  
s = list(s)  
left, right = 0, len(s) - 1
    
while left < right:
    if s[left] not in vowels:
        left += 1
    elif s[right] not in vowels:
        right -= 1
    else:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    
return ''.join(s)

