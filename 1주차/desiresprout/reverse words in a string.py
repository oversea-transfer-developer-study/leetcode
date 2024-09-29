# 1. Problem 
# Given an input string s, your task is to reverse the order of words in the string. A word is defined as a sequence of non-space characters, and words are separated by one or more spaces

# 2. Test case
# 	Input: the sky is blue
# 	Output: blue is sky the
			
# 	Input: "  hello world  "
# 	Output: world hello
		
	
# 3. Plan
# 	we can split the string, sort them in reverse, and then combine them
	
	
# Time Complexity: O(n)
# Space Complexity: O(n)

s = s.split()
s.reverse()
return "".join(s)



