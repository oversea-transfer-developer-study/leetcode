# 1. Problem 
# Given two strings, merge them in alternating order 
# we have to start with a certain letter and choose it.

	
# 2. Test case
# 	abc,pqr => qpbqcr
# 	ab,pqrs => apbqrs
# 	abcd,pq => apbqcd
	
# 3. Plan
# 	1) find the length between word1 and word2
# 	2) merge string from word1 and word2 and make it list
# 	3) turn the list into string
	
# Time Complexity: O(n1 + n2) 
# — we iterate through the shorter string in the first step and append the remaining part in the second step.
# Space Complexity: O(n1 + n2) 
# — to store the result
	
n1, n2 = len(word1), len(word2)
merged_string = [word1[i] + word2[i] for i in range(min(n1, n2))] 
merged_string.append(word1[min(n1, n2):] + word2[min(n1, n2):])
return ''.join(merged_string)